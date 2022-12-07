def warboy(A, B, C):
    return (B // A) * 3 * C
    

if __name__ == "__main__":
    A, B, C = map(int, input().split())
    
    print(warboy(A=A, B=B, C=C))