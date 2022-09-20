from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    for n in course:
        tmp = []
        for order in orders:
            order_list = list(order)
        
            combination_list = combinations(order_list, n)
            for combination in combination_list:
                tmp.append("".join(sorted(combination)))


        counter_list = Counter(tmp).most_common()
        if len(counter_list) == 0:
            continue 
        # print(counter_list)
        max_cnt = counter_list[0][1]
        if max_cnt <= 1:
            continue

        for value, cnt in counter_list:
            if cnt == max_cnt:
                answer.append(value)
            else:
                break
    
    return sorted(answer)