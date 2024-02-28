from faker import Faker
import random
from tqdm import tqdm
from babel.dates import format_date
from datetime import date, timedelta
import json


fake = Faker()
Faker.seed(234235)
random.seed(32534235)

RANGE_DENSITY = 0.7 # number of ranges / total
MAX_RANGE     = 31
MIN_RANGE     = 1
CHAR_PAD      = '@'
CHAR_UNK      = '^'

# Define format of the data we would like to generate

DATES_FROM = [ # DATE FROM
	'short',
	'medium',
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
	' - ',
	'/',
	'/ ',
	' /',
	' / ',
	' ',
	' to '
]

DATES_TO = [
	'short',
	'medium',
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

FORMATS = (
	('dd', 'dd/mm', 'ddmm&&&&', 'ddmm&&&&')
)




# change this if you want it to work with another language
LOCALES = ['en_US']

def generate_date(date, format):
	try:
		return (
			format_date(date, format=format, locale='en_GB').lower().replace(',',''),
			date.isoformat().replace('-', '')
		)
	except AttributeError as e:
		return None, None

def compile_range(dt_from, dt_to):
	dt_from_h, dt_from_m = generate_date(dt_from, random.choice(DATES_FROM))
	if dt_to:
		dt_to_h, dt_to_m = generate_date(dt_to, random.choice(DATES_TO))
		delimiter = random.choice(DELIMITERS)
		print(delimiter)
	else:
		delimiter = ''
		dt_to_h   = ''
		dt_to_m   = CHAR_PAD * 8
	
	return (
		f'{dt_from_h}{delimiter}{dt_to_h}',
		f'{dt_from_m}{dt_to_m}'
	)

def load_date_range():
	is_range   = random.random() < RANGE_DENSITY
	range_days = timedelta(days=random.randint(MIN_RANGE, MAX_RANGE))
	
	dt_from = fake.date_object()
	dt_to   = dt_from + range_days if is_range else None
	return compile_range(dt_from, dt_to)

def load_dataset(m):
	human_vocab = set()
	machine_vocab = set()
	dataset = []

	for i in tqdm(range(m)):
		h, m = load_date_range()
		if h is not None:
			dataset.append((h, m))
			human_vocab.update(tuple(h))
			machine_vocab.update(tuple(m))

	human = dict(zip(
		sorted(human_vocab) + [CHAR_UNK, CHAR_PAD],
		list(range(len(human_vocab) + 2))
	))
	inv_machine = dict(enumerate(sorted(machine_vocab)))
	machine = {v:k for k,v in inv_machine.items()}

	return dataset, human, machine, inv_machine

if __name__ == '__main__':
	for d in load_dataset(1001)[0]:
		print(d[0])

