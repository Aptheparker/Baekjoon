N = int(input())

member = []

for i in range(N):
    age, name = list(map(str, input().split()))
    member.append((int(age), name))
                  
member.sort(key=lambda x : x[0])

for j in range(N):
    print(member[j][0], member[j][1])