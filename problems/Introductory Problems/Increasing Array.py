l = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(1,l):
	if a[i] < a[i-1]:
		count = count + a[i-1] - a[i]
		a[i] = a[i-1]
print(count)
