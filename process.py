import re

FILE_NAME = 'data.txt'

SUFFIX  = ('th','nd','st','rd')
ALPHA_MONTHS = (
	('jan','january'),
	('fb','feb', 'february'),
	('mrch', 'march'),
	('ap', 'apr', 'april'),
	('my', 'may'),
	('jn', 'jun', 'june'),
	('jl', 'jul', 'july', 'juli'),
	('au', 'aug', 'augst', 'august'),
	('sep', 'sept', 'septmbr', 'september'),
	('okt', 'oct', 'octbr', 'october', 'oktober'),
	('nv', 'nov', 'nvmb', 'nvmbr', 'novemb', 'november'),
	('dc', 'dec', 'decmbr', 'december')
)
ALPHA_DOW = (
	'mn', 'mnd', 'mon', 'mond', 'monday',
	'tu', 'tue', 'tues', 'tuesdy', 'tuesday',
	'wd', 'wed', 'wedn', 'wednsdy', 'wednesday',
	'th', 'thu', 'thur', 'thrsdy', 'thursday',
	'fr', 'fry', 'fri', 'fridy', 'friday',
	'st', 'sat', 'satur', 'saturdy', 'saturday',
	'sn', 'sun', 'sund', 'sundy', 'sunday'
)
SEP = ['.', '/', '-', ' ']
PAR = [')', '(']


class String:
  @staticmethod
  def is_alpha(s):
    return bool(re.match(r'^[\p{L} ]+$', s))

  @staticmethod
  def has_numbers(s):
    return bool(re.search(r'\d', s))

  @staticmethod
  def is_int(s):
    return bool(re.match(r'^\d+$', s))

  @staticmethod
  def is_float(s):
    return bool(re.match(r'^\d+(\.\d+)?$', s))

  @staticmethod
  def from_alpha_month(s):
  	for n in range(len(ALPHA_MONTHS)):
  		if s in ALPHA_MONTHS[n]:
  			return n + 1
  	return 0

  @staticmethod
  def is_alpha_dow(s):
  	return s in ALPHA_DOW

  @staticmethod
  def is_sep(s):
  	return s in SEP

  @staticmethod
  def is_suffix(s):
  	return s in SUFFIX

  @staticmethod
  def is_par(s):
  	return s in PAR


def clean_string(s):
	# Replace tabs and newlines with spaces
	s = s.replace('\t', ' ').replace('\n', ' ').lower()
	# Iteratively replace double spaces with single spaces until no more double spaces are found
	while '  ' in s:
		s = s.replace('  ', ' ')
	return s

def get_dates(filename):
	with open(filename) as f:
		text = f.read()
	return [clean_string(s) for s in text.split('\n')]

def split_and_keep_delimiters(s, delimiters):
    # Add a space to the list of delimiters, if it's not already included
    if ' ' not in delimiters:
        delimiters.append(' ')
    # Create a regular expression pattern that matches the delimiters
    # The pattern uses a capture group to retain the delimiters
    # Also, add patterns to split between alphabetic and numeric characters
    pattern = f'([{"".join(map(re.escape, delimiters))}]|(?<=[0-9])(?=[A-Za-z])|(?<=[A-Za-z])(?=[0-9]))'
    # Use re.split with the pattern and retain the delimiters
    return re.split(pattern, s)

def collapse_consecutive_unk(a):
	is_unk = False
	result = ''
	for t in a:
		if t == 'u':
			if not is_unk:
				result += t
			is_unk = True
		elif not String.is_sep(t):
			is_unk = False
			result += t
		elif String.is_sep(t) and not is_unk:
			result += t
		else:
			result += t
	return result


def process_date(date):
	tokens    = split_and_keep_delimiters(date, SEP + PAR)
	formula   = ''
	variables = []
	for token in tokens:
		if (month := String.from_alpha_month(token)) != 0:
			formula += 'm'
			variables.append(month)
		elif String.is_int(token):
			if len(token) <= 2:
				formula += 'n'
			else:
				formula += 'N'
			variables.append(int(token))
		elif String.is_sep(token):
			formula += token
		elif String.is_par(token):
			formula += token
		elif String.is_suffix(token):
			formula += 's'
		elif token == '':
			pass
		else:
			formula += 'u'

	formula = collapse_consecutive_unk(formula) \
		.replace(' )', ')') \
		.replace('( ', '(') \
		.replace('  ', ' ') \
		.replace('- ', '-') \
		.replace(' -', '-') \
		.replace('/ ', '/') \
		.replace(' /', '/') \
		.strip(''.join(SEP))

	print(date.ljust(35), (formula).ljust(15), variables)
	return formula, variables
	

dates = get_dates(FILE_NAME)

formulas  = []
variables = []

for date in dates:
	f, v = process_date(date)
	formulas.append(f)
	variables.append(v)

print(len(formulas), len(list(set(formulas))))

for f in list(set(formulas)):
	print(f)















