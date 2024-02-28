triads = (
	'nnn',
	'nnN',
	'nmn',
	'nmN',

	'n/n/n',
	'n/n/N',
	'n/m/n',
	'n/m/N',

	'n-n-n',
	'n-n-N',
	'n-m-n',
	'n-m-N',


	'Nnn',
	'Nnn',
	'Nmn',
	'Nmn',

	'N/n/n',
	'N/n/n',
	'N/m/n',
	'N/m/n',

	'N-n-n',
	'N-n-n',
	'N-m-n',
	'N-m-n',


	'mnn',
	'mnN',

	'm-n-n',
	'm-n-N',

	'm/n/n',
	'm/n/N',
)

delims = ('', '/', '-')


def get_delim(s):
	for c in s:
		if c in '-/':
			return c
	return ''

def get_other_delim(d):
	return '-' if d == '/' else '/'

def can_go_first(s):
	d = get_delim(s)
	return d == '' or d == '/'

def get_month_pos(s):
	pos = 0
	for c in s:
		if c in 'mnN':
			pos += 1
		if c == 'm':
			return pos
	return -1

def get_post_formula(x, y, mx, my, d):
	if mx == -1:
		if my == -1:

		else:
	else:
		if my == -1:

		else:


def run(triads):
	unique   = set()
	formulas = []
	mx, my
	for x in triads:
		mx = get_month_pos(x)
		for y in triads:
			my = get_month_pos(y)
			for d in delims:
				if can_go_first(x):
					if get_delim(x) != d and get_delim(y) != d:
						f1 = f'{x}{d}{y}'
						f2 = get_post_formula(x, y, mx, my, d)
						if f1 not in unique:
							formulas.append([f1, f2])
							unique.add(f1)
	return formulas

formulas = run(triads)





















