#input
while True:
  num = int(input())
  l1 = []
  total = 0


#control
  if num == -1:
    exit(0)
    
  for i in range(1, num):
    if num % i == 0:
      l1.append(i)
    else:
      continue
      
  for j in range(0, len(l1)):
    total += l1[j]
    if total == num:
      l2 = [str(x) for x in l1]
      output = str(num) + " = " + " + ".join(l2)
    else: 
      output = str(num) + ' is NOT perfect.'

#output
  print(output)