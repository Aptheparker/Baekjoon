def equality(string):
    answer = "NO"
    
    num1, operator, num2, equal_sign, num3 = string.split()
    
    if int(num1) + int(num2) == int(num3):
        answer = "YES"
        
    return answer


if __name__ == "__main__":
    string = input()
    print(equality(string))