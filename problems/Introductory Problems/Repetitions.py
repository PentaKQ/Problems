s = input()
count = 1
max = 0
for i in range(1,len(s)):
	if s[i] == s[i-1]:
		count = count+1
	else:
		if count > max:
			max = count
		count = 1
if count > max:
			max = count
if max == 0:		
	print(count)
else:
	print(max)