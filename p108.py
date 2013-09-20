import math
def sieve(n): 
	if n < 2:
		return []
	elif n < 4:
		return [2]
	n, correction = n-n%6+6, 2-(n%6>1)
	b = [True] * (n/3)
	for i in xrange(1,int(n**0.5)/3+1):
		if b[i]:
			k = 3*i + 1 | 1
			b[ (k**2)/3 :: 2*k] = [False]*((n/6 - (k**2)/6 - 1)/k + 1)
			b[k*(k-2*(i & 1) + 4)/3 :: 2*k] = [False]*((n/6 - k*(k - 2*(i&1) + 4)/6 - 1)/k + 1)
	return [2,3] + [3*i+1|1 for i in xrange(1, n/3 - correction) if b[i]]
primes = sieve(10000000)
num = 1000
def f(n):
	count = 1
	i = 0
	ans = 1
	while n > 1 and primes[i]*primes[i] <= n: 
		while n % primes[i] == 0 : 
			count = count + 2
			n /= primes[i]
		ans = ans * count
		count = 1
		i = i + 1
	if n > 1 : ans *= 3
	return ans / 2 + 1
n = 1000
while f(n) <= num:
	n = n + 1
print n 