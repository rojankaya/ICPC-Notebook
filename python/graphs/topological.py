from collections import deque


def topological_sort(g):
	n = len(g)
	deg = [0] * n

	for u in range(n):
		for v in g[u]:
			deg[v] += 1

	q = deque(i for i in range(n) if deg[i] == 0)
	order = []

	while q:
		u = q.popleft()
		order.append(u)

		for v in g[u]:
			deg[v] -= 1
			if deg[v] == 0:
				q.append(v)

	return order if len(order) == n else None


# None means the graph contains a cycle
