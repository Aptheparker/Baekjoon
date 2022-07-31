#input
T = int(input())
a = list(map(int, input().split()))

#control
maxNum = max(a)
minNum = min(a)

#output
print(minNum, maxNum)