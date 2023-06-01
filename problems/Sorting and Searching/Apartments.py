n, m, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
#n, m, k = 10,10,10
#a = [90, 41, 20, 39, 49, 21, 35, 31, 74, 86]
#b = [14 ,24, 24, 7, 82, 85, 82, 4, 60, 95]
a.sort()
b.sort()
countroom = 0
count = 0
for h in range(n):
		if a[h] > b[m-1] + k or a[h] < b[0] - k:
			continue
		else:
			for i in range(countroom,m):
				if a[h] <= b[i] + k and a[h] >= b[i]-k:
					count = count+1
					countroom = i+1
					break
print(count)