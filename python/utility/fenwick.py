class Fenwick:
	def __init__(self, n):
		self.n = n
		self.bit = [0] * (n + 1)

	def add(self, i, x):
		i += 1
		while i <= self.n:
			self.bit[i] += x
			i += i & -i

	def sum(self, i):
		# Sum of [0, i)
		s = 0
		while i:
			s += self.bit[i]
			i -= i & -i
		return s

	def query(self, l, r):
		# Sum of [l, r)
		return self.sum(r) - self.sum(l)

	def lower_bound(self, x):
		# Smallest i such that sum(i + 1) >= x.
		# Requires x > 0.
		i = 0
		k = 1 << (self.n.bit_length() - 1)
		while k:
			j = i + k
			if j <= self.n and self.bit[j] < x:
				i = j
				x -= self.bit[j]
			k >>= 1
		return i
