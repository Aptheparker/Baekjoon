def convert_first_word_upper(string):
    string = string[0].upper() + string[1:]
    
    return string


if __name__ == "__main__":
    for _ in range(int(input())):
        string = input()
        print(convert_first_word_upper(string))