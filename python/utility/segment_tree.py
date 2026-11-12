class SegTree:
	def __init__(self, a, op=min, e=float("inf")):
		self.n = len(a)
		self.op = op
		self.e = e
		self.t = [e] * (2 * self.n)
		self.t[self.n :] = a

		for i in range(self.n - 1, 0, -1):
			self.t[i] = op(self.t[2 * i], self.t[2 * i + 1])

	def set(self, i, x):
		i += self.n
		self.t[i] = x
		i >>= 1
		while i:
			self.t[i] = self.op(self.t[2 * i], self.t[2 * i + 1])
			i >>= 1

	def query(self, l, r):
		# [l, r)
		l += self.n
		r += self.n
		res_l = self.e
		res_r = self.e

		while l < r:
			if l & 1:
				res_l = self.op(res_l, self.t[l])
				l += 1
			if r & 1:
				r -= 1
				res_r = self.op(self.t[r], res_r)
			l >>= 1
			r >>= 1

		return self.op(res_l, res_r)


# For sums: st = SegTree(a, op=lambda x, y: x + y, e=0)
