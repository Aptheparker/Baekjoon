I1, M1, S1, E1 = map(int, input().split())
I2, M2, S2, E2 = map(int, input().split())

total1 = I1 + M1 + S1 + E1
total2 = I2 + M2 + S2 + E2

if total1==total2:
  print(total1)
else:
  print(max(total1, total2))



