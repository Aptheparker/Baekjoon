N, K = map(int, input().split())
answer = []
    
people = list(range(1, N+1))
    
popNum = 0 
    
while len(people) > 0: 
    popNum = (popNum + (K-1)) % len(people) 
    popElemnet = people.pop(popNum) 
    answer.append(str(popElemnet))
        
print(f"<{', '.join(answer)}>")