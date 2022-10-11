import sys

a = sys.stdin.readline()
b = sys.stdin.readline()

c = bin(int(a,2) * int(b,2))[2:]

print(c)