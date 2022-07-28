case = int(input())

for i in range(case):
  R, S = input().split()
  iteration = ''
  for j in S:
    iteration += int(R) * j
  print(iteration)