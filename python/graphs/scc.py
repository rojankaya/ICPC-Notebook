def scc(g):
	n = len(g)
	rg = [[] for _ in range(n)]

	for u in range(n):
		for v in g[u]:
			rg[v].append(u)

	seen = [False] * n
	order = []

	for s in range(n):
		if seen[s]:
			continue

		seen[s] = True
		st = [(s, 0)]

		while st:
			u, i = st[-1]

			if i < len(g[u]):
				v = g[u][i]
				st[-1] = (u, i + 1)

				if not seen[v]:
					seen[v] = True
					st.append((v, 0))
			else:
				order.append(u)
				st.pop()

	comp = [-1] * n
	k = 0

	for s in reversed(order):
		if comp[s] != -1:
			continue

		comp[s] = k
		st = [s]

		while st:
			u = st.pop()
			for v in rg[u]:
				if comp[v] == -1:
					comp[v] = k
					st.append(v)

		k += 1

	return comp, k


# comp[u] == comp[v] iff u and v belong to the same SCC
