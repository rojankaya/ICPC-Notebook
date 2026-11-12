def crt(a, m):
	# x = a[i] (mod m[i])
	# Assumes pairwise coprime moduli.
	x = 0
	mod = 1

	for ai, mi in zip(a, m):
		k = ((ai - x) * mod_inverse(mod, mi)) % mi
		x += mod * k
		mod *= mi

	return x % mod, mod


# Returns (x, lcm(moduli))
