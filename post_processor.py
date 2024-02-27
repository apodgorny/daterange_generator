from datetime import datetime

from constants import TOKEN_CURRENT


class PostProcessor:
	@staticmethod
	def is_current(s):
		return s == TOKEN_CURRENT

	@classmethod
	def _generate_date(cls, formula, variables):
		if len(formula):
			now   = datetime.now()
			day   = now.day   if cls.is_current(formula[0]) else variables[int(formula[0])] 
			month = now.month if cls.is_current(formula[1]) else variables[int(formula[1])]
			year  = now.year  if cls.is_current(formula[2]) else variables[int(formula[2])]

			return datetime(int(year), int(month), int(day))
		return None

	@classmethod
	def generate_dates(cls, formula, variables):
		return (
			cls._generate_date(formula[:3], variables),
			cls._generate_date(formula[3:], variables)
		)
	