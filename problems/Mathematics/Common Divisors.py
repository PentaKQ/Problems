#n = int(input())
#a = [int(i) for i in input().split()]
f = open("D:\\Python\\test_input.txt", "r")
n = f.readline()
a = f.readline()
f.close()
a = a.split(',')
#n = 5
#a = [3,14,15,7,9]
print(a)
max = 1
before1 = 0
before2 = 0
a.sort(reverse=True)
for i in range(n-1):
	for k in range(a[i]-1):
		k = k+1
		z = a[i]/k
		if z == before1:
			continue
		before1 = z
		h = i+1
		while h<=n-1:
			for kk in range(a[h]-1):
				kk = kk+1
				zz = a[h]/kk
				if zz == before2:
					continue
				before2 = zz
				if zz == z:
					if z > max:
						max = z
						break
			h = h + 1
print(round(max))

