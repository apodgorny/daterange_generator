import re

from library.string import String, SEP, PAR
from constants      import *


class PreProcessor:
	@staticmethod
	def clean_string(s):
		# Replace tabs and newlines with spaces
		s = s.replace('\t', ' ').replace('\n', ' ').lower()
		s = s.replace('–', '-')
		# Iteratively replace double spaces with single spaces until no more double spaces are found
		while '  ' in s:
			s = s.replace('  ', ' ')
		s = PreProcessor.replace_spaced_characters(s)
		return s

	@staticmethod
	def replace_spaced_characters(s): # thins like "t o d a y"
		# Regular expression pattern to match sequences of single spaced characters
		pattern = r'\b(?:[a-zA-Z] )+[a-zA-Z]\b'
		# Replace found patterns with their unspaced version
		return re.sub(pattern, lambda x: ''.join(x.group().split()), s)

	@staticmethod
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
	
	@staticmethod
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
	
	@classmethod
	def get_dates(cls, filename):
		with open(filename) as f:
			text = f.read()
		return [cls.clean_string(s) for s in text.split('\n')]

	@classmethod
	def process_date(cls, date):
		sep1      = None
		sep2      = None
		tokens    = cls.split_and_keep_delimiters(date, SEP + PAR)
		formula   = ''
		variables = []
		for token in tokens:
			if (month := String.from_alpha_month(token)) != 0:
				formula += TOKEN_MONTH
				variables.append(month)
			elif String.is_int(token):
				if len(token) <= 2:
					formula += TOKEN_NUM_SM
				else:
					formula += TOKEN_NUM_LG
				variables.append(int(token))
			elif String.is_sep(token):
				if token != ' ':
					if not sep1:
						sep1 = token
						formula += TOKEN_SEP1
					elif sep1 != token:
						sep2 = token
						formula += TOKEN_SEP2
					else:
						if token == sep1:
							formula += TOKEN_SEP1
						else:
							formula += TOKEN_SEP2
			elif String.is_par(token):
				formula += token
			elif String.is_suffix(token):
				pass
			elif String.is_after_word(token):
				formula += TOKEN_AFTER
			elif String.is_begin_word(token):
				formula += TOKEN_BEGIN
			elif String.is_end_word(token):
				formula += TOKEN_END
			elif String.is_now_word(token):
				formula = '&&&'
				break
			elif token == '':
				pass
			else:
				# formula += TOKEN_UNK
				pass

		formula = cls.collapse_consecutive_unk(formula) \
			.replace(' )', ')') \
			.replace('( ', '(') \
			.replace('  ', ' ') \
			.replace('- ', '-') \
			.replace(' -', '-') \
			.replace('/ ', '/') \
			.replace(' /', '/') \
			.strip(''.join(SEP))

		return formula, variables
	