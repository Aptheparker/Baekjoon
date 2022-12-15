a=input()
b=input()
c=input()
d=input()
e=input()
f=input()
sum=0

for i in [a,b,c,d,e,f]:
    if i == 'W':
        i = 1
    else:
        i=0
    sum += i

if sum>=5:
    print(1)
elif sum>=3:
    print(2)
elif sum>=1:
    print(3)
else:
    print(-1)

