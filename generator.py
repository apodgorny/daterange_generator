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

def get_year_pos(s):
	pos = 0
	for c in s:
		if c in 'mnN':
			pos += 1
		if c == 'N':
			return pos
	return -1

def get_post_formula(mx, my, yx, yy):
	f = ''
	has_month_x = mx != -1
	has_month_y = my != -1
	has_year_x  = yx != -1
	has_year_y  = yy != -1

	
	if not has_month_x:
		if not has_month_y:
			if not has_year_x:
				if not has_year_y:
					# nnn nnn
					...
				else:
					if yy == 2:
						# nnn nnN
						...
					if yy == 0:
						# nnn Nnn
						...
			else:
				if not has_year_y:
					if yx == 2:
						# nnN nnn
						...
					if yx == 0:
						# Nnn nnn
						...
				else:
					if yx == 2:
						if yy == 2:
							# nnN nnN
							...
						if yy == 0:
							# nnN Nnn
							...
					if yx == 0:
						if yy == 2:
							# Nnn nnN
							...
						if yy == 0:					
							# Nnn Nnn
							...
		else:
			if not has_year_x:
				if not has_year_y:
					if my == 1:
						# nnn nmn
						...
					if my == 0:
						# nnn mnn
						...
				else:
					if my == 1:
						if yy == 2:
							# nnn nmN
							...
						if yy == 0:
							# nnn Nmn
							...
					if my == 0:
						if yy == 2:
							# nnn mnN
							...
			else:
				if not has_year_y:
					if my == 1:
						if yx == 2:
							# nnN nmn
							...
					if my == 0:
						if yx == 0:
							# Nnn mnn
							...
				else:
					if my == 0:
						if yx == 2:
							if yy == 2:
								# nnN mnN
								...
						if yx == 0:
							if yy == 2:
								# Nnn mnN
								...
					if my == 1:
						if yx == 2:
							if yy == 2:
								# nnN nmN
								...
							if yy == 0:
								# nnN Nmn
								...
						if yx == 0:
							if yy == 2:
								# Nnn nmN
								...
							if yy == 0:
								# Nnn Nmn
								...
	else:
		if not has_month_y:
			if not has_year_x:
				if not has_year_y:
					if mx == 1:
						# nmn nnn
						...
					if mx == 0:
						# mnn nnn
						...
				else:
					if mx == 1:
						if yy == 2:
							# nmn nnN
							...
						if yy == 0:
							# nmn Nnn
							...
					if mx == 0:
						if yy == 2:
							# mnn nnN
							...
						if yy == 0:
							# mnn Nnn
							...
			else:
				if not has_year_y:
					if mx == 1:
						if yx == 2:
							# nmN nnn
							...
						if yx == 0:
							# Nmn nnn
							...
					if mx == 0:
						if yx == 2:
							# mnN nnn
							...
				else:
					if mx == 1:
						if yx == 2:
							if yy == 2:
								# nmN nnN
								...
							if yy == 0:
								# nmN Nnn
								...
						if yx == 0:
							if yy == 2:
								# Nmn nnN
								...
							if yy == 0:
								# Nmn Nnn
								...
					if mx == 0:
						if yx == 2:
							if yy == 2:
								# mnN nnN
								...
							if yy == 0:
								# mnN Nnn
								...
		else:
			if not has_year_x:
				if not has_year_y:
					if mx == 1:
						if my == 1:
							# nmn nmn
							...
						if my == 0:
							# nmn mnn
							...
					if mx == 0:
						if my == 1:
							# mnn nmn
							...
						if my == 0:
							# mnn mnn
							...
				else:
					if mx == 1:
						if my == 1:
							if yy == 2:
								# nmn nmN
								...
							if yy == 0:
								# nmn Nmn
								...
						if my == 0:
							if yy == 2:
								# nmn mnN
								...
					if mx == 0:
						if my == 1:
							if yy == 2:
								# mnn nmN
								...
							if yy == 0:
								# mnn Nmn
								...
						if my == 0:
							if yy == 2:
								# mnn mnN
								...
			else:
				if not has_year_y:
					if mx == 1:
						if my == 1:
							if yx == 2:
								# nmN nmn
								...
							if yx == 0:
								# Nmn nmn
								...
						if my == 0:
							if yx == 2:
								# nmN mnn
								...
							if yx == 0:
								# Nmn mnn
								...
					if mx == 0:
						if my == 1:
							# mnN nmn
							...
						if my == 0:
							# mnN mnn
							...
				else:
					if mx == 1:
						if my == 1:
							if yx == 2:
								if yy == 2:	
									# nmN nmN
									...
								if yy == 0:
									# nmN Nmn
									...
							if yx == 0:
								if yy == 2:
									# Nmn nmN
									...
								if yy == 0:
									# Nmn Nmn
									...
						if my == 0:
							if yx == 2:
								if yy == 2:
									# nmN mnN
									...
							if yx == 0:
								if yy == 2:
									# Nmn mnN
									...
					if mx == 0:
						if my == 1:
							if yx == 2:
								if yy == 2:
									# mnN nmN
									...
								if yy == 0:
									# mnN Nmn
									...
						if my == 0:
							if yx == 2:
								if yy == 2:
									# mnN mnN
									...
						

def run(triads):
	unique   = set()
	formulas = []
	mx, my
	yx, yy
	for x in triads:
		mx = get_month_pos(x)
		yx = get_year_pos(x)
		for y in triads:
			my = get_month_pos(y)
			yy = get_year_pos(y)
			for d in delims:
				if can_go_first(x):
					if get_delim(x) != d and get_delim(y) != d:
						f1 = f'{x}{d}{y}'
						f2 = get_post_formula(mx, my, yx, yy)
						if f1 not in unique:
							formulas.append([f1, f2])
							unique.add(f1)
	return formulas

formulas = run(triads)





















