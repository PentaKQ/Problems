n = int(input())
a = []
b = []
for i in range(n):
	x,y = [int(k) for k in input().split()]
	a.append(x)
	b.append(y)
minb = 0
count = 0
z = 0
f = n
while n>0:
	mina = 1000
	check = False
	for i in range(n):
		if n == f:
			if mina > a[i]:
				mina = a[i]
				minb = b[i]
				z = i
				check = True
				continue
			if mina == a[i] and minb > b[i]:
				minb = b[i]
				z = i
		else:
			if mina > a[i] and a[i] >= minb:
				mina = a[i]
				z = i
				check = True
				continue
			if mina == a[i] and minb > b[i]:
				z = i
		minb = b[z]
	if check:
		count = count + 1
	a.pop(z)
	b.pop(z)
	n = n - 1
print(count)