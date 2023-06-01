n = int(input())
x = list(map(int,input().split()))
# n = 10
# x = [1,1,1,1,1,1,1,1,1,1]
count = []
c = 0
i = 0
while len(x) != 0:
        k = x[i]
        try:
                while x.index(k) != -1:
                        x.remove(k)
        except:
                c += 1

print(c)