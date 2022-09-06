A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())

total1 = A+B+C+D - min(A,B,C,D)
total2 = max(E,F)

print(total1 + total2)