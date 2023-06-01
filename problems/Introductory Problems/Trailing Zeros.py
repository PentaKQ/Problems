n = int(input())
s = 1
st = ''
count = 0
max = 0
for i in range(1,n+1):
	s = s*i
st = str(s)
for i in range(len(st)):
	if st[i]=='0':
		count = count + 1
	if st[i]!='0':
		max = count
		count = 0
max = count
print(max)