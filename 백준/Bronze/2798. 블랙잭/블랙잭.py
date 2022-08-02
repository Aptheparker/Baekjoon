from itertools import combinations

def blackjack(M, card_numbers):
    comb_3 = list(combinations(card_numbers, 3))
    
    sum_list = [sum(comb) for comb in comb_3 if sum(comb) <= M]
    
    return max(sum_list)


N, M = map(int, input().split())
    
card_numbers = list(map(int, input().split()))
    
print(blackjack(M, card_numbers))