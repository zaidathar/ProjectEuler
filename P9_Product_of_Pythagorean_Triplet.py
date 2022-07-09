from collections import defaultdict
import math
d=defaultdict(int)

for a in range(1,1500):
    for b in range(a+1,1500):
        c=math.sqrt(a**2+b**2)
        s=a+b+c
        d[s]=a*b*c
t=int(input())

for _ in range(t):
    n=int(input())
    res=d[n]
    if res==0:
        print(-1)
    else:
        print(int(res))
