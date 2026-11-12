def bipartite(g):
	n = len(g)
	color = [-1] * n

	for s in range(n):
		if color[s] != -1:
			continue

		color[s] = 0
		st = [s]

		while st:
			u = st.pop()

			for v in g[u]:
				if color[v] == -1:
					color[v] = color[u] ^ 1
					st.append(v)
				elif color[v] == color[u]:
					return False, None

	return True, color
