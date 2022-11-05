def barn_subscription(N, W, H, L):
    answer = N
    width_cow = W // L
    height_cow = H // L
    
    cow_num = width_cow * height_cow
    
    if cow_num < N:
        answer = cow_num
        
    return answer 


if __name__ == "__main__":
    N, W, H, L = map(int, input().split())
    print(barn_subscription(N, W, H, L))