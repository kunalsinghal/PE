def mul(a,b):
	return [a[0]*b[0]+2*a[1]*b[1],a[1]*b[0]+a[0]*b[1]]
I = [1,0]
start = [1,1]
val = [1,1]
while True : 
	if (val[0] & 1) == 1 and (val[0] & 1) == 1: 
		if (val[0]+1)/2 >= 10**12 : 
			print (val[1]+1)/2
			break
	val = mul(val,start)
