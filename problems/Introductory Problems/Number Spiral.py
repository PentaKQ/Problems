k = int(input())
for h in range(k):
	y,x = [int(i) for i in input().split()]
	if x == 1:
		if y % 2 == 0:
			print(y*y)
			continue
		else:
			print((y-1)*(y-1)+1)
			continue
	if y == 1:
		if x % 2 == 0:
				print((x-1)*(x-1)+1)
				continue
		else:
			print((x)*(x))
			continue
	if y < x:
		if x % 2 == 0:
			num = (x-1)*(x-1)+1
			print(num+(y-1))
			continue
		else:
			num = (x)*(x)
			print(num-(y-1))
			continue
	if y == x:
		if x % 2 == 0:
			num = (x-1)*(x-1)+1
			print(num+(y-1))
			continue
		else:
			num = (x)*(x)
			print(num-(y-1))
			continue
	if y > x:
		if y % 2 == 0:
			num = (y)*(y)
			print(num-(x-1))
			continue
		else:
			num = (y-1)*(y-1)+1
			print(num+(x-1))
			continue
