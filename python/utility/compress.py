def compress(a):
	vals = sorted(set(a))
	pos = {x: i for i, x in enumerate(vals)}
	return [pos[x] for x in a], vals


# Example: b, vals = compress(a)
