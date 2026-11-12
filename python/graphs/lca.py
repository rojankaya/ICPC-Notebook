class LCA:
	def __init__(self, g, root=0):
		n = len(g)
		self.log = n.bit_length()

		self.up = [[-1] * n for _ in range(self.log)]
		self.depth = [-1] * n

		self.depth[root] = 0
		st = [root]

		while st:
			u = st.pop()

			for v in g[u]:
				if self.depth[v] == -1:
					self.depth[v] = self.depth[u] + 1
					self.up[0][v] = u
					st.append(v)

		for j in range(1, self.log):
			prev = self.up[j - 1]
			cur = self.up[j]

			for v in range(n):
				p = prev[v]
				cur[v] = -1 if p == -1 else prev[p]

	def kth(self, u, k):
		j = 0

		while k:
			if k & 1:
				u = self.up[j][u]
				if u == -1:
					return -1
			k >>= 1
			j += 1

		return u

	def query(self, u, v):
		if self.depth[u] < self.depth[v]:
			u, v = v, u

		u = self.kth(u, self.depth[u] - self.depth[v])

		if u == v:
			return u

		for j in range(self.log - 1, -1, -1):
			if self.up[j][u] != self.up[j][v]:
				u = self.up[j][u]
				v = self.up[j][v]

		return self.up[0][u]
