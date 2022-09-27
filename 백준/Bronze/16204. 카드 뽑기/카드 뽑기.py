N,M,K = map(int, input().split())

total1 = min(M, K)
total2 = min(N-M, N-K)

print(total1+total2)
