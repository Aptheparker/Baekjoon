#input
a,b,c,d,e = map(int, input().split())

#control
output = (a**2 + b**2 + c**2 + d**2 + e**2) % 10

#output
print(output)