a = int(input())


for i in range(1,a):
  print(i*'*',end = "")
  print(2*(a-i)*' ',end = "")
  print(i*'*')
for i in range(0,a):
  print((a-i)*'*',end = "")
  print(i*2*' ',end = "")
  print((a-i)*'*')