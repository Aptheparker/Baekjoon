ans = int(input())
a,b,c,d,e = map(int, input().split())
score = 0

for i in (a,b,c,d,e):
	if i == ans:
		score+=1
	else:
		continue

print(score)