n = int(input())
lst1=list(input().split())
m=int(input())
lst2=list(input().split())

lst1.sort()
chk_num = {}
for i in lst1:
    if i not in chk_num:
        chk_num[i] = 1
    else:
        chk_num[i] += 1

for i in lst2:
    try: print(chk_num[i], end=" ")
    except: print(0, end=" ")