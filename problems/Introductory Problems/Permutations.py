a = int(input())
if a == 2 or a == 3:
	print('NO SOLUTION')
	exit()
if a == 1:
	print('1')
	exit()
for i in range(1,a+1):
	if i % 2 == 0:
		print(i)
for i in range(1,a+1):
	if i % 2 != 0:
		print(i)
