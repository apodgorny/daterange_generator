from faker import Faker
import random
from tqdm import tqdm
from babel.dates import format_date
from datetime import date, timedelta



fake = Faker()
Faker.seed(12345)
random.seed(12345)

RANGE_DENSITY = 0.7 # number of ranges / total
MAX_RANGE     = 31
MIN_RANGE     = 1

# Define format of the data we would like to generate

DATES_FROM = [ # DATE FROM
	'short',
	'medium',
	'long',
	'full',
	'full',
	'full',
	'full',
	'full',
	'full',
	'full',
	'full',
	'full',
	'full',
	'd MMM YYY',
	'd MMMM YYY',
	'dd MMM YYY',
	'd MMM, YYY',
	'd MMMM, YYY',
	'dd, MMM YYY',
	'd MM YY',
	'd MMMM YYY',
	'MMMM d YYY',
	'MMMM d, YYY',
	'dd.MM.YY'
]

DELIMITERS = [
	'-',
	' -',
	'- ',
	' - '
	'/',
	'/ ',
	' /',
	' / ',
	' '
]

DATES_TO = [
	'short',
	'medium',
	'long',
	'full',
	'full',
	'full',
	'full',
	'full',
	'full',
	'full',
	'full',
	'full',
	'full',
	'd MMM YYY',
	'd MMMM YYY',
	'dd MMM YYY',
	'd MMM, YYY',
	'd MMMM, YYY',
	'dd, MMM YYY',
	'd MM YY',
	'd MMMM YYY',
	'MMMM d YYY',
	'MMMM d, YYY',
	'dd.MM.YY'
]

# change this if you want it to work with another language
LOCALES = ['en_US']

def generate_date(date, format):
	try:
		human_readable = format_date(date, format=format,  locale='en_US') # locale=random.choice(LOCALES))
		human_readable = human_readable.lower()
		human_readable = human_readable.replace(',','')
		machine_readable = date.isoformat().replace('-', '')

	except AttributeError as e:
		return None, None

	return human_readable, machine_readable

def compile_range(dt_from, dt_to):
	dt_from_human_readable, dt_from_machine_readable = generate_date(dt_from, random.choice(DATES_FROM))
	if dt_to:
		dt_to_human_readable,   dt_to_machine_readable   = generate_date(dt_to, random.choice(DATES_TO))
		delimiter = random.choice(DELIMITERS)
		return f'{dt_from_human_readable}{delimiter}{dt_to_human_readable}', f'{dt_from_machine_readable}{dt_to_machine_readable}'
	else:
		return dt_from_human_readable, f'{dt_from_machine_readable}{8*"<pad>"}'

def load_date_range():
	"""
		Loads some fake dates
		:returns: tuple containing human readable string, machine readable string, and date object
	"""
	is_range = random.random() < RANGE_DENSITY
	
	dt_from = fake.date_object()
	dt_to   = dt_from + timedelta(days=random.randint(MAX_RANGE, MIN_RANGE)) if is_range else None
	return compile_range(dt_from, dt_to)


def load_dataset(m):
	"""
		Loads a dataset with m examples and vocabularies
		:m: the number of examples to generate
	"""

	human_vocab = set()
	machine_vocab = set()
	dataset = []
	Tx = 30


	for i in tqdm(range(m)):
		h, m = load_date_range()
		if h is not None:
			dataset.append((h, m))
			human_vocab.update(tuple(h))
			machine_vocab.update(tuple(m))

	human = dict(zip(sorted(human_vocab) + ['<unk>', '<pad>'],
					 list(range(len(human_vocab) + 2))))
	inv_machine = dict(enumerate(sorted(machine_vocab)))
	machine = {v:k for k,v in inv_machine.items()}

	return dataset, human, machine, inv_machine

if __name__ == '__main__':
	print(load_dataset(10))