sum1=0
sum2=0
sum3=0

a=int(input())

for i in range(a):
  num=int(input())
  sum1+=num

b=int(input())

for i in range(b):
  num=int(input())
  sum2+=num
  
c=int(input())

for i in range(c):
  num=int(input())
  sum3+=num

for i in (sum1,sum2,sum3):
  if i == 0:
    print(0)
  elif i<0:
    print('-')
  else:
    print('+')