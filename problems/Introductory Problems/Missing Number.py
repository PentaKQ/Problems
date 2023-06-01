n = int(input())
a = [int(i) for i in input().split()]
z = 0
count = True
check = True
a.sort()
for i in range(n-1):
	if a[i] != i+1:
		print(i+1)
		count = False
		break
if count == True:
	print(n)