
def split_formula(pre):
	alpha = 'nmN'
	alpha_count1 = 0
	alpha_count2 = 0
	n = 0

	for ch in pre:
		if ch in alpha:
			alpha_count1 += 1

	if alpha_count1 == 6:
		for ch in pre:
			if ch in alpha:
				alpha_count2 += 1
				if alpha_count2 == 3:
					n += 1
					break
			n += 1
		return pre[:n].strip('/-'), pre[n:].strip('/-')
	return None


with open('data/dataset.csv') as f:
	lines = f.read().split('\n')

triads = set()
for line in lines:
	pre, post = line.split(',')
	if pair := split_formula(pre):
		triads.add(pair[0])
		triads.add(pair[1])

print(list(triads))


# 4
# n/nmN ('n/nm', 'N')
# 4
# n/nm ('n/nm', '')
# 4
# n/n-n-N ('n/n-', 'n-N')
# 4
# nm/nmN ('nm/n', 'mN')
# 4
# n/nmn ('n/nm', 'n')
# 4
# n/n-n ('n/n-', 'n')