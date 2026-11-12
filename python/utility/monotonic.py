def next_greater(a):
	n = len(a)
	ans = [-1] * n
	st = []

	for i, x in enumerate(a):
		while st and a[st[-1]] < x:
			ans[st.pop()] = i
		st.append(i)

	return ans


def sliding_min(a, k):
	from collections import deque

	q = deque()
	ans = []

	for i, x in enumerate(a):
		while q and q[0] <= i - k:
			q.popleft()
		while q and a[q[-1]] >= x:
			q.pop()

		q.append(i)

		if i >= k - 1:
			ans.append(a[q[0]])

	return ans
