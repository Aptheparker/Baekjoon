N, X, A, Y, B = map(int, input().split())
 
X_temp=0;
Y_temp=0;
 
for i in range(1, N+1, 1):
    if (X*i >= N):
        X_temp = A*i;
        break;
 
for i in range(1, N+1, 1):
    if (Y*i >= N):
        Y_temp = B*i;
        break;
 
print(min(X_temp, Y_temp))