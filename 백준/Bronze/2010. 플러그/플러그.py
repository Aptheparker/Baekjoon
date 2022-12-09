N= int(input())
plugs=0
plugs+=int(input())

for i in range(N-1):
  plugs+=int(input())
  plugs-=1

print(plugs)