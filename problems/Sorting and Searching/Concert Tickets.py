n,x = [int(i) for i in input().split()]
gv = [int(i) for i in input().split()]
gk = [int(i) for i in input().split()]
#n,x = 10,5
#gv = [5,3,7,8,5,6,4,98,5,3]
#gk = [4,8,3,5,4]
gv.sort()
i=0
k = 0
if n == 1:
	while k <= x-1:
		if gk[k] == gv[i]:
			gv.pop(i)
			print(gk[k])
			k = k + 1
			i = 0
		else:
			print(-1)
else:			
	if x == 1:
		for i in range(n-1):
			if gk[0] == gv[i]:
				print(gk[0])
				break
			if gk[k] > gv[i] and gk[k] < gv[i+1]:
				print(gv[i])
				break
	else:
		while k <= x-1:
			i = 0
			while i <= n-2:
				if gk[k]<gv[0]:
					print(-1)
					k = k + 1
					i = 0
					break
				if gk[k] == gv[n-1]:
					gv.pop(n-1)
					n = n - 1
					print(gk[k])
					k = k + 1
					i = 0
					continue
				if gk[k] == gv[i]:
					gv.pop(i)
					n = n - 1
					print(gk[k])
					k = k + 1
					i = 0
					continue
				else:
					if gk[k] > gv[i] and gk[k] < gv[i+1]:
						print(gv[i])
						gv.pop(i)
						n = n - 1
						k = k +1
						i = 0
						continue
				i = i + 1