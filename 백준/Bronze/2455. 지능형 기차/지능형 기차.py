a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
c1,c2=map(int,input().split())
d1,d2=map(int,input().split())

sum1 = 0-a1+a2
sum2 = sum1-b1+b2
sum3 = sum2-c1+c2
sum4=sum3-d1+d2

print(max(sum1,sum2,sum3,sum4))