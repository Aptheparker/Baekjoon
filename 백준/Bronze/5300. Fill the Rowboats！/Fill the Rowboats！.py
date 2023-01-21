a  =int(input())

for i in range(1,a+1):
  print(i, end=" ")
  if i%6==0 or i==a:
    print("Go!", end=" ")