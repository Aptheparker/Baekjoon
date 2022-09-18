A,B,C = map(int, input().split())

t1 = A*B/C
t2 = A/B*C

print(int(max(t1, t2)))