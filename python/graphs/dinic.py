from collections import deque


class Dinic:
	def __init__(self, n):
		self.n = n
		self.g = [[] for _ in range(n)]

	def add_edge(self, u, v, cap):
		self.g[u].append([v, cap, len(self.g[v])])
		self.g[v].append([u, 0, len(self.g[u]) - 1])

	def max_flow(self, s, t):
		flow = 0
		inf = 10**30

		while True:
			level = [-1] * self.n
			level[s] = 0
			q = deque([s])

			while q:
				u = q.popleft()

				for v, cap, rev in self.g[u]:
					if cap > 0 and level[v] == -1:
						level[v] = level[u] + 1
						q.append(v)

			if level[t] == -1:
				return flow

			it = [0] * self.n

			def dfs(u, f):
				if u == t:
					return f

				while it[u] < len(self.g[u]):
					e = self.g[u][it[u]]
					v, cap, rev = e

					if cap > 0 and level[v] == level[u] + 1:
						x = dfs(v, min(f, cap))

						if x:
							e[1] -= x
							self.g[v][rev][1] += x
							return x

					it[u] += 1

				return 0

			while True:
				f = dfs(s, inf)
				if not f:
					break
				flow += f
