from collections import deque


def hopcroft_karp(g, n_right):
	n_left = len(g)

	pair_u = [-1] * n_left
	pair_v = [-1] * n_right
	dist = [0] * n_left

	def bfs():
		q = deque()

		for u in range(n_left):
			if pair_u[u] == -1:
				dist[u] = 0
				q.append(u)
			else:
				dist[u] = -1

		found = False

		while q:
			u = q.popleft()

			for v in g[u]:
				w = pair_v[v]

				if w == -1:
					found = True
				elif dist[w] == -1:
					dist[w] = dist[u] + 1
					q.append(w)

		return found

	def dfs(u):
		for v in g[u]:
			w = pair_v[v]

			if w == -1 or (dist[w] == dist[u] + 1 and dfs(w)):
				pair_u[u] = v
				pair_v[v] = u
				return True

		dist[u] = -1
		return False

	matching = 0

	while bfs():
		for u in range(n_left):
			if pair_u[u] == -1 and dfs(u):
				matching += 1

	return matching, pair_u, pair_v
