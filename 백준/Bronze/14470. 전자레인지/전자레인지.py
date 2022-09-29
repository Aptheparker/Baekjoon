A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

total=0

if A>0 and B>0:
  total = (B-A)*E
elif A<0 and B>0:
  total = abs(A)*C + D + B*E
else:
  total = (B-A)*C


print(total)