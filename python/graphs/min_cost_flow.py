import heapq


class MinCostFlow:
	def __init__(self, n):
		self.n = n
		self.g = [[] for _ in range(n)]

	def add_edge(self, u, v, cap, cost):
		self.g[u].append([v, cap, cost, len(self.g[v])])
		self.g[v].append([u, 0, -cost, len(self.g[u]) - 1])

	def flow(self, s, t, max_flow=10**30):
		n = self.n
		flow = cost = 0
		potential = [0] * n

		while flow < max_flow:
			inf = 10**30
			dist = [inf] * n
			prev = [None] * n
			dist[s] = 0

			pq = [(0, s)]

			while pq:
				d, u = heapq.heappop(pq)

				if d != dist[u]:
					continue

				for i, (v, cap, c, rev) in enumerate(self.g[u]):
					if cap:
						nd = d + c + potential[u] - potential[v]

						if nd < dist[v]:
							dist[v] = nd
							prev[v] = (u, i)
							heapq.heappush(pq, (nd, v))

			if dist[t] == inf:
				break

			for v in range(n):
				if dist[v] < inf:
					potential[v] += dist[v]

			add = max_flow - flow
			v = t

			while v != s:
				u, i = prev[v]
				add = min(add, self.g[u][i][1])
				v = u

			v = t

			while v != s:
				u, i = prev[v]
				e = self.g[u][i]
				e[1] -= add
				self.g[v][e[3]][1] += add
				cost += add * e[2]
				v = u

			flow += add

		return flow, cost
