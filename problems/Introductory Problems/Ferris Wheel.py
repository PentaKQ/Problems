#n,x = [int(i) for i in input().split()]
#a = [int(i) for i in input().split()]
n,x = 10,50
a = []
a.sort()
count = 0
xx = x
countnum = 0
check = False
i = 0
while n != 0:
	check = False
	k = n-1
	while k >= i:
		if i == k:
			count = count + 1
			a.remove(a[i])
			n = n - 1
			break
		if a[i] + a[k] <= xx:
			xx = xx - (a[i]+a[k])
			a.remove(a[k])
			n = n - 1
			check = True
		elif check:
			count = count + 1
			xx = x
			a.remove(a[i])
			n = n-1
			break
		k = k - 1
print(count)

