class SparseTable:
	def __init__(self, a, op=min):
		self.op = op
		n = len(a)

		self.log = [0] * (n + 1)
		for i in range(2, n + 1):
			self.log[i] = self.log[i >> 1] + 1

		k = self.log[n] + 1
		self.st = [a]

		for j in range(1, k):
			p = self.st[-1]
			length = 1 << j
			half = length >> 1
			self.st.append([op(p[i], p[i + half]) for i in range(n - length + 1)])

	def query(self, l, r):
		# [l, r)
		k = self.log[r - l]
		return self.op(self.st[k][l], self.st[k][r - (1 << k)])
