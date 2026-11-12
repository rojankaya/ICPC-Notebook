from math import gcd


def factorize(n):
	f = []

	while n % 2 == 0:
		f.append(2)
		n //= 2

	p = 3

	while p * p <= n:
		while n % p == 0:
			f.append(p)
			n //= p
		p += 2

	if n > 1:
		f.append(n)

	return f
