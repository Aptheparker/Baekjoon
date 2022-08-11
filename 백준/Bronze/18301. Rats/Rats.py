import math
n1,n2,n3 = map(int, input().split())

N = math.floor((n1+1)*(n2+1)/(n3+1)-1)

print(N)