#input
N, X = map(int, input().split())
A = list(map(int, input().split()))


#control
for i in A:
    if int(i) < X:
        print(i, end = ' ')

#output
