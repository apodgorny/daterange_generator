import calendar

from datetime       import datetime

from constants      import TOKEN_CURRENT, TOKEN_AFTER, TOKEN_BEGIN, TOKEN_END
from library.string import String


class PostProcessor:
	def __init__(self):
		self.date_from = None

	@staticmethod
	def is_current(s):
		return s == TOKEN_CURRENT

	@staticmethod
	def is_after(s):
		return s == TOKEN_AFTER

	@staticmethod
	def days_in_month(m, y):
		return calendar.monthrange(y, m)[1]

	@staticmethod
	def _handle_begin_word(formula, variables):
		for n in range(len(formula)):
			if String.is_int(formula[n]):
				formula = String.char(formula, n, str(int(formula[n]) + 1))

		formula   = String.char(formula, 0, '0')
		variables = [1] + variables

		return formula, variables

	@staticmethod
	def _handle_end_word(formula, variables):
		for n in range(len(formula)):
			if String.is_int(formula[n]):
				formula = String.char(formula, n, str(int(formula[n]) + 1))

		formula   = String.char(formula, 0, '0')
		variables = [28] + variables
		
		return formula, variables

	def _generate_date(self, formula, variables):
		if len(formula):
			if formula[0] == TOKEN_BEGIN:
				formula, variables = self._handle_begin_word(formula, variables)

			if formula[0] == TOKEN_END:
				formula, variables = self._handle_end_word(formula, variables)

			d, m, y = formula
			now     = datetime.now()

			if self.is_current(y):
				year = now.year
			elif self.is_after(y):
				if self.date_from:
					year = self.date_from.year + 1
			else:
				year = variables[int(y)]

			if self.is_current(m):
				month = now.month
			elif self.is_after(m):
				if self.date_from:
					month = self.date_from.month + 1
					month = month if month <= 12 else 1
			else:
				month = variables[int(m)]

			if self.is_current(d):
				day = now.day
			elif self.is_after(d):
				if self.date_from:
					day = self.date_from.day + 1
					day = day if day <= self.days_in_month(month, year) else 1
			else:
				day = variables[int(d)]

			
			return datetime(int(year) or 2000, int(month), int(day))
		return None

	def __call__(self, formula, variables):
		self.date_from = self._generate_date(formula[:3], variables)
		return (
			self.date_from,
			self._generate_date(formula[3:], variables)
		)
	