def bridges(g):
	n = len(g)
	tin = [-1] * n
	low = [0] * n
	timer = 0
	ans = []
	cut = [False] * n

	def dfs(u, p):
		nonlocal timer

		tin[u] = low[u] = timer
		timer += 1
		children = 0

		for v in g[u]:
			if v == p:
				continue

			if tin[v] != -1:
				low[u] = min(low[u], tin[v])
			else:
				dfs(v, u)
				low[u] = min(low[u], low[v])

				if low[v] > tin[u]:
					ans.append((u, v))

				if p != -1 and low[v] >= tin[u]:
					cut[u] = True

				children += 1

		if p == -1 and children > 1:
			cut[u] = True

	for i in range(n):
		if tin[i] == -1:
			dfs(i, -1)

	return ans, cut
