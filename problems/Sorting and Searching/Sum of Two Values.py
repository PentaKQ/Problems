n , x = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
#n , x = 3,5
#a = [1,2,3]

for i in range(n-1):
	for k in range(i+1,n):
		if a[i] + a[k] == x:
			print(i+1,k+1)
			exit()
		if sum(a)<x:
			print('IMPOSSIBLE')
			exit()
print('IMPOSSIBLE')