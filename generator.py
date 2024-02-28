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
	pos = -1
	for c in s:
		if c in 'mnN':
			pos += 1
		if c == 'm':
			return pos
	return -1

def get_year_pos(s):
	pos = -1
	for c in s:
		if c in 'mnN':
			pos += 1
		if c == 'N':
			return pos
	return -1

def get_post_formula(x, y):
	translation = {
		'mnn' : [1, 0, 2],
		'nnn' : [0, 1, 2],
		'nmn' : [0, 1, 2],
		'mnN' : [1, 0, 2],
		'Nmn' : [2, 1, 0],
		'nmN' : [0, 1, 2],
		'Nnn' : [2, 1, 0],
		'nnN' : [0, 1, 2]
	}

	fx = translation[get_simple_triad(x)]
	fy = translation[get_simple_triad(y)]

	return ''.join(map(str, fx)) + ''.join([str(n + 3) for n in fy])

def get_simple_triad(s):
	return s.replace('-', '').replace('/', '')

def run(triads):
	unique   = set()
	formulas = []
	mx, my   =  None, None
	yx, yy   =  None, None
	for x in triads:
		mx = get_month_pos(x)
		yx = get_year_pos(x)
		for y in triads:
			my = get_month_pos(y)
			yy = get_year_pos(y)
			for d in delims:
				if can_go_first(x):
					if get_delim(x) != d and get_delim(y) != d:
						pre = f'{x}{d}{y}'
						if pre not in unique:
							post = get_post_formula(x, y)
							formulas.append([pre, post])
							unique.add(pre)
	return formulas

formulas= run(triads)

for pre, post in formulas:
	print(pre.ljust(25), post)

print(len(formulas))




















