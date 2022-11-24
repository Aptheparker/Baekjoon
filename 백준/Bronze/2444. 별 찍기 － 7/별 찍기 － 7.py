a = int(input())


for i in range(1,a+1):
  print((a-i)*' ',end = "")
  print((2*i-1)*'*')
for i in range(1,a):
  print(i*' ',end = "")
  print((2*(a-i)-1)*'*')