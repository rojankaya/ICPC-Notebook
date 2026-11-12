def extgcd(a, b):
	if b == 0:
		return a, 1, 0

	g, x, y = extgcd(b, a % b)
	return g, y, x - (a // b) * y
