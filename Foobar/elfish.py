def elfish(s):
	f_e=False
	f_l=False
	f_f=False
	for i in s:
		if i=="e":
			f_e=True
		if i=="l":
			f_l=True
		if i=="f":
			f_f=True
	if f_e and f_l and f_f:
		return True
	else:
		return False
print(elfish(input()))