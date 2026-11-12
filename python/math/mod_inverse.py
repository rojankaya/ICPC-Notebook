def mod_inverse(a, mod):
	g, x, _ = extgcd(a, mod)

	if g != 1:
		return None

	return x % mod


# For prime mod, pow(a, -1, mod) is also available in modern Python, but keeping the explicit implementation is useful for the notebook
