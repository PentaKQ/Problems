n = int(input())
a = [int(i) for i in input().split()]
#n = 10
# = [952, 775, 292, 702 ,859 ,719, 65, 943, 376, 490]
g1 = a[n-1]
g2 = sum(a)-a[n-1]
max = abs(g2-g1)
for k in range(n):
	g1 = a[n-1]
	g2 = sum(a)-a[n-1]
	for i in range(k,n):
		g1 = g1 + a[i]
		g2 = g2 - a[i]
		if abs(g1-g2)<max:
			max = abs(g1-g2)
g1 = 0
g2 = 0
z = 0
for i in range(n):
	if i % 2 == 0:
		g1 = g1 + a[i]
	else:
		g2 = g2 + a[i]
if abs(g1-g2)<max:
	max = abs(g1-g2)
print(max)