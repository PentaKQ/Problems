n = int(input())
for i in range(n):
	check = True
	sum = 0
	a, b = [int(h) for h in input().split()]
	if a == 0 and b != 0 or b == 0 and a != 0:
		print('NO')
		check = False
	if check:
			if a == b:
				if a % 3 == 0:
					print('YES')
					check = False
				else:
					print('NO')
					check = False
	if check:
		if a>b and a/2<=b or a<b and b/2<=a:
			a = str(a)
			b = str(b)
			for x in range(len(a)):
				sum = sum + int(a[x])
			for y in range(len(b)):
				sum = sum + int(b[y])
			if sum % 3 == 0:
				print('YES')
				check = False
	if check:
		print('NO')

