import re
def reg(cc):
	regex = r'\d+'
	matches = re.findall(regex, cc)
	match = ''.join(matches)
	n = match[:16]
	mm = match[16:18]
	yy = match[18:20]
	if yy == '20':
		yy = match[18:22]
		if n.startswith("3"):
			cvc = match[22:26]
		else:
			cvc = match[22:25]
	else:
		if n.startswith("3"):
			cvc = match[20:24]
		else:
			cvc = match[20:23]
	cc = f"{n}|{mm}|{yy}|{cvc}"
	if not re.match(r'^\d{16}$', n):
		return
	if not re.match(r'^\d{3,4}$', cvc):
		return
	return cc
	