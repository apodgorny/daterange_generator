class Parser:
	NUMERIC = '0123456789'
	ALPHA   = 'abcdefghijklmnopqrstuvwxyz'
	SPACE   = ' \n\t\r'
	DELIM   = '-/'
	SEP     = './-'
	SUFFIX  = ('th','nd','st','rd')
	ALPHA_MONTHS = (
		'jan','january',
		'fb','feb', 'february',
		'mrch', 'march',
		'ap', 'apr', 'april',
		'my', 'may',
		'jn', 'jun', 'june',
		'jl', 'jul', 'july', 'juli',
		'au', 'aug', 'augst', 'august',
		'sep', 'sept', 'septmbr', 'september',
		'okt', 'oct', 'octbr', 'october', 'oktober',
		'nv', 'nov', 'nvmb', 'nvmbr', 'novemb', 'november'
		'dc', 'dec', 'decmbr', 'december'
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

	def __init__(self):
		self.n = 0
		self.s = ''
		self._mark = 0

	def next(self):
		self.n += 1
		if self.n == len(self.s):
			raise Exception('eof')

	def unwind(self):
		self.n = self.mark

	def mark(self):
		self.mark = self.n

	def char(self):
		return self.s[self.n]

	def get(self, charset):
		value = ''
		while self.char() in Parser.NUMERIC:
			value += self.char()
			self.next()
		return value

	def get_numeric(self):
		return self.get(Parser.NUMERIC)

	def get_space(self):
		return self.get(Parser.SPACE)

	def get_alpha(self):
		return self.get(Parser.ALPHA)

	def get_delimiter(self):
		b = self.get(Parser.ALPHA)
		return b != ''

	def get_date_sep(self):
		self.mark()
		value = self.get(Parser.SEP)
		if len(value) == 1:
			return True
		else:
			self.unwind()
		return False

	def get_suffix(self):
		self.mark()
		value = self.get_alpha()
		if value in Parser.SUFFIX:
			return value
		else:
			self.unwind()
			return False

	def get_alpha_month():
		self.mark()
		value = self.get_alpha()
		if value in Parser.ALPHA_MONTHS:
			return value
		else:
			self.unwind()
			return False

	def get_alpha_dow():
		self.mark()
		value = self.get_alpha()
		if value in Parser.ALPHA_DOW:
			return value
		else:
			self.unwind()
			return False

	def get_num_day():
		self.mark()
		value = self.get_numeric()
		if len(value) <= 2:
			self.get_suffix()
			return value
		else:
			self.unwind()
			return False

	def get_num_month():
		self.mark()
		value = self.get_numeric()
		if len(value) <= 2:
			return value
		else:
			self.unwind()
			return False

	def get_num_year():
		self.mark()
		value = self.get_numeric()
		if len(value) in [2,4]:
			return value
		else:
			self.unwind()
			return False

	def get_first_date():
		value = []
		self.get_alpha_dow():
		value.append(self.get_num_day())
		self.get_suffix()
		if self.
		return value

	def parse(self, s):
		self.s = s
		self.n = 0
		self.get_first_date()
		self.get_space()
		self.get_delimiter()
		self.get_space()
		self.get_second_date()




