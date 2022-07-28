h, m, s = map(int, input().split())
t = int(input())
print((h+((s+t)//60 + m)//60)%24, ((s+t)//60 + m)%60, (s+t)%60)