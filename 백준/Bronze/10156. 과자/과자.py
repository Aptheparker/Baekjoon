K, N, M = map(int, input().split())

if M >= K * N:
  res = 0
else:
  res = K * N -M

print(res)