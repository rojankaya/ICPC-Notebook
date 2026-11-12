def two_sat(n, clauses):
	# Clause: (a or b)
	# Literal x: x >= 0 means x, x < 0 means not x.
	# Variable i is represented by 2*i = false, 2*i+1 = true.

	g = [[] for _ in range(2 * n)]

	def node(x):
		return 2 * x if x >= 0 else 2 * (-x - 1) + 1

	def neg(x):
		return x ^ 1

	for a, b in clauses:
		a = node(a)
		b = node(b)
		g[neg(a)].append(b)
		g[neg(b)].append(a)

	comp, _ = scc(g)

	ans = [False] * n

	for i in range(n):
		if comp[2 * i] == comp[2 * i + 1]:
			return None

		ans[i] = comp[2 * i] < comp[2 * i + 1]

	return ans


# The two_sat function assumes the literal convention:
# x      # variable x
# -x - 1 # negation of variable x
# So (x0 OR NOT x1) is:
# (0, -2)
