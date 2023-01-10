n=int(input())

for i in range(n):
  dog,food,price=map(float,input().split())
  print(f'${dog*food*price:.2f}')