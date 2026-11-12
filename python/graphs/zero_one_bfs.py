from collections import deque


def zero_one_bfs(g, s):
	# g[u] contains (v, w), w in {0, 1}
	n = len(g)
	inf = 10**30
	dist = [inf] * n
	dist[s] = 0

	q = deque([s])

	while q:
		u = q.popleft()

		for v, w in g[u]:
			nd = dist[u] + w

			if nd < dist[v]:
				dist[v] = nd

				if w == 0:
					q.appendleft(v)
				else:
					q.append(v)

	return dist
