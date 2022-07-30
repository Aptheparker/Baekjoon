#input
H, M = map(int, input().split())

#control
t = 45
if M >= 45:
  H = H
  M -= t
else:
  H -= 1
  remain = t - M
  M = 60 - remain

if H < 0:
  H += 24

print(H,M)