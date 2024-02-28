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
					f = '012345'
				else:
					if yy == 2:
						# nnn nnN
						f = '012345'
					if yy == 0:
						# nnn Nnn
						f = '012453'
			else:
				if not has_year_y:
					if yx == 2:
						# nnN nnn
						f = '012345'
					if yx == 0:
						# Nnn nnn
						f = '210345'
				else:
					if yx == 2:
						if yy == 2:
							# nnN nnN
							f = '012345'
						if yy == 0:
							# nnN Nnn
							f = '012543'
					if yx == 0:
						if yy == 2:
							# Nnn nnN
							f = '210345'
						if yy == 0:					
							# Nnn Nnn
							f = '210543'
		else:
			if not has_year_x:
				if not has_year_y:
					if my == 1:
						# nnn nmn
						f = '012345'
					if my == 0:
						# nnn mnn
						f = '012435'
				else:
					if my == 1:
						if yy == 2:
							# nnn nmN
							f = '012345'
						if yy == 0:
							# nnn Nmn
							f = '012543'
					if my == 0:
						if yy == 2:
							# nnn mnN
							f = '012435'
			else:
				if not has_year_y:
					if my == 1:
						if yx == 2:
							# nnN nmn
							f = '012345'
					if my == 0:
						if yx == 0:
							# Nnn mnn
							f = '210435'
				else:
					if my == 0:
						if yx == 2:
							if yy == 2:
								# nnN mnN
								f = '012435'
						if yx == 0:
							if yy == 2:
								# Nnn mnN
								f = '210435'
					if my == 1:
						if yx == 2:
							if yy == 2:
								# nnN nmN
								f = '012345'
							if yy == 0:
								# nnN Nmn
								f = '012543'
						if yx == 0:
							if yy == 2:
								# Nnn nmN
								f = '210345'
							if yy == 0:
								# Nnn Nmn
								f = '210543'
	else:
		if not has_month_y:
			if not has_year_x:
				if not has_year_y:
					if mx == 1:
						# nmn nnn
						f = '012345'
					if mx == 0:
						# mnn nnn
						f = '102345'
				else:
					if mx == 1:
						if yy == 2:
							# nmn nnN
							f = '012345'
						if yy == 0:
							# nmn Nnn
							f = '012543'
					if mx == 0:
						if yy == 2:
							# mnn nnN
							f = '102345'
						if yy == 0:
							# mnn Nnn
							f = '102543'
			else:
				if not has_year_y:
					if mx == 1:
						if yx == 2:
							# nmN nnn
							f = '012345'
						if yx == 0:
							# Nmn nnn
							f = '210345'
					if mx == 0:
						if yx == 2:
							# mnN nnn
							f = '102345'
				else:
					if mx == 1:
						if yx == 2:
							if yy == 2:
								# nmN nnN
								f = '012345'
							if yy == 0:
								# nmN Nnn
								f = '012543'
						if yx == 0:
							if yy == 2:
								# Nmn nnN
								f = '210345'
							if yy == 0:
								# Nmn Nnn
								f = '210543'
					if mx == 0:
						if yx == 2:
							if yy == 2:
								# mnN nnN
								f = '102345'
							if yy == 0:
								# mnN Nnn
								f = '102543'
		else:
			if not has_year_x:
				if not has_year_y:
					if mx == 1:
						if my == 1:
							# nmn nmn
							f = '012345'
						if my == 0:
							# nmn mnn
							f = '012435'
					if mx == 0:
						if my == 1:
							# mnn nmn
							f = '102345'
						if my == 0:
							# mnn mnn
							f = '102435'
				else:
					if mx == 1:
						if my == 1:
							if yy == 2:
								# nmn nmN
								f = '012345'
							if yy == 0:
								# nmn Nmn
								f = '012543'
						if my == 0:
							if yy == 2:
								# nmn mnN
								f = '012435'
					if mx == 0:
						if my == 1:
							if yy == 2:
								# mnn nmN
								f = '102345'
							if yy == 0:
								# mnn Nmn
								f = '102543'
						if my == 0:
							if yy == 2:
								# mnn mnN
								f = '102435'
			else:
				if not has_year_y:
					if mx == 1:
						if my == 1:
							if yx == 2:
								# nmN nmn
								f = '012345'
							if yx == 0:
								# Nmn nmn
								f = '210345'
						if my == 0:
							if yx == 2:
								# nmN mnn
								f = '012435'
							if yx == 0:
								# Nmn mnn
								f = '210435'
					if mx == 0:
						if my == 1:
							# mnN nmn
							f = '102345'
						if my == 0:
							# mnN mnn
							f = '102435'
				else:
					if mx == 1:
						if my == 1:
							if yx == 2:
								if yy == 2:	
									# nmN nmN
									f = '012345'
								if yy == 0:
									# nmN Nmn
									f = '012543'
							if yx == 0:
								if yy == 2:
									# Nmn nmN
									f = '210345'
								if yy == 0:
									# Nmn Nmn
									f = '210543'
						if my == 0:
							if yx == 2:
								if yy == 2:
									# nmN mnN
									f = '012435'
							if yx == 0:
								if yy == 2:
									# Nmn mnN
									f = '210435'
					if mx == 0:
						if my == 1:
							if yx == 2:
								if yy == 2:
									# mnN nmN
									f = '102345'
								if yy == 0:
									# mnN Nmn
									f = '102543'
						if my == 0:
							if yx == 2:
								if yy == 2:
									# mnN mnN
									f = '102435'
	return f

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
						pre  = f'{x}{d}{y}'
						post = get_post_formula(mx, my, yx, yy)
						if pre not in unique:
							formulas.append([pre, post])
							unique.add(pre)
	return formulas

formulas = run(triads)

for pre, post in formulas:
	print(f'{pre} : {post}')





















