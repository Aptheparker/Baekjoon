lst = sorted(list(map(int, input().split())))

if lst[0] == lst[1] or lst[1] == lst[2] or lst[0]+lst[1] == lst[2]:
    print("S")
else:
    print("N")
    