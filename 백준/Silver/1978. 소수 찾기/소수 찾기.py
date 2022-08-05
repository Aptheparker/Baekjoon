T = int(input())
numbers = list(map(int, input().split()))
count = 0

for i in numbers:
  checker = 0

  if i == 1:
    continue
  
  for j in range(2, i):
    if i % j == 0:
      checker += 1

  if checker == 0:
    count+=1

    
      

print(count)
  

  

