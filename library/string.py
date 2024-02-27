import re

SUFFIX  = ('th','nd','st','rd')

AFTER = ('onw','onward','after','later','afterwards')
BEGIN = ('beg','begin','early','start')
END   = ('end','late')
NOW   = ('now', 'today')

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
	def char(s, n, c=None):
		if c is not None:
			return s[:n] + c + s[n + 1:]
		return s[n]

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

	@staticmethod
	def is_after_word(s):
		return s in AFTER

	@staticmethod
	def is_begin_word(s):
		return s in BEGIN

	@staticmethod
	def is_end_word(s):
		return s in END

	@staticmethod
	def is_now_word(s):
		return s in NOW
		
	