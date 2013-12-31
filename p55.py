def check(n):
    return 1 if str(n) == str(n)[::-1] else 0

inp = 10**4
lis = [0 for i in xrange(inp)]

for k in reversed(range(inp)):
    val = 0
    i = k
    for _ in xrange(50):
        i += int(str(i)[::-1])
        if i < inp:
            val = max(check(i),lis[i])
            break
        else :
            val = check(i)
        if val == 1:
            break
    lis[k] = val

lis = map(lambda x: 1^x, lis)
print sum(lis)
