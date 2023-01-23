n= int(input())

lst=[]

for i in range(n):
    x,y=map(int,input().split())
    lst.append([x,y])

for i in lst:
    level=1
    for j in lst:
        if j[0]>i[0] and j[1]>i[1]:
            level+=1
        elif j[0]<=i[0] and j[1]>i[1] or j[0]>i[0] and j[1]<=i[1]:
            level+=0

    print(level,end=" ")