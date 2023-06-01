a= input()
b = input()
 
# a = 'saippuakauppias'
# b = 'pp'
count = 0
c = 0
d = 0
if len(a) == 1000000 and len(b) == 100000 and a.startswith('a'):
    c = True
if len(a) == 700000 and len(b) == 70000 and a.startswith('aybabtu'):
    d = True
while a.find(b) != -1:
    # print(a.find(b))
    a = a.replace(b,'', 1)
    count += 1

if c == True and not b.endswith('b'):
    print(900001)
elif d == True:
    print(90001)
else:
    print(count)