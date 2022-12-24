def get_perfect_square_numbers():
    return [pow(num, 2) for num in range(1, 101)]

def perfect_square(num1, num2, perfect_square_numbers):
    square_num = [num for num in perfect_square_numbers if num1 <= num <= num2]
    
    if len(square_num) == 0:
        answer = [-1]
    else:
        answer = sum(square_num), min(square_num)
    
    return answer
    
    
    
if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    
    perfect_square_numbers = get_perfect_square_numbers()
    answer = perfect_square(num1, num2, perfect_square_numbers)
    
    for num in answer:
        print(num)