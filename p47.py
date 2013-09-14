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
l = sieve(100000)
def check(x):
	cnt = 0
	i = 0
	while x > 0 and cnt < 5 and i*i <= x : 
		if x % l[i] == 0 :
			while x % l[i] == 0 : x /= l[i]
			cnt += 1
		i += 1
	if x > 1 : cnt += 1
	return cnt == 4
		
for i in range(10,1000000):
	if check(i) and check(i+1) and check(i+2) and check(i+3): 
		print i
		break