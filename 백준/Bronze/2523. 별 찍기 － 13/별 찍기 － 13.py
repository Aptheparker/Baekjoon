def print_stars(N):
    for i in range(1, N + 1):
        print(f"{'*' * i}")
    for i in range(N - 1, 0, -1):
        print(f"{'*' * i}")
              
if __name__ == "__main__":
    N = int(input())
    print_stars(N)