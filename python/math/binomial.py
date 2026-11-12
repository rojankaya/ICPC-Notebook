class Binomial:
	def __init__(self, n, mod):
		self.mod = mod
		self.fact = [1] * (n + 1)
		self.invfact = [1] * (n + 1)

		for i in range(1, n + 1):
			self.fact[i] = self.fact[i - 1] * i % mod

		self.invfact[n] = pow(self.fact[n], mod - 2, mod)

		for i in range(n, 0, -1):
			self.invfact[i - 1] = self.invfact[i] * i % mod

	def choose(self, n, k):
		if k < 0 or k > n:
			return 0

		return self.fact[n] * self.invfact[k] * self.invfact[n - k] % self.mod


# This assumes mod is prime and n < mod
