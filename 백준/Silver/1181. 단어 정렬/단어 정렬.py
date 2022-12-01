N = int(input())

words = []

for i in range(N):
    word = input()
    
    if (len(word), word) not in words:
        words.append((len(word), word))
    
answer = sorted(words, key=lambda x: (x[0], x[1]))

for ans in answer:
    print(ans[1])