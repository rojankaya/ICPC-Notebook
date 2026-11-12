from collections import deque


class AhoCorasick:
	def __init__(self, patterns):
		self.next = [{}]
		self.link = [0]
		self.out = [[]]

		for idx, s in enumerate(patterns):
			u = 0

			for c in s:
				if c not in self.next[u]:
					self.next[u][c] = len(self.next)
					self.next.append({})
					self.link.append(0)
					self.out.append([])

				u = self.next[u][c]

			self.out[u].append(idx)

		q = deque()

		for v in self.next[0].values():
			q.append(v)

		while q:
			u = q.popleft()

			for c, v in self.next[u].items():
				q.append(v)

				p = self.link[u]

				while p and c not in self.next[p]:
					p = self.link[p]

				self.link[v] = self.next[p].get(c, 0)
				self.out[v].extend(self.out[self.link[v]])

	def find(self, text):
		u = 0
		ans = []

		for i, c in enumerate(text):
			while u and c not in self.next[u]:
				u = self.link[u]

			u = self.next[u].get(c, 0)

			for pattern in self.out[u]:
				ans.append((i, pattern))

		return ans


# find(text) returns (ending_position, pattern_id) for every occurrence
