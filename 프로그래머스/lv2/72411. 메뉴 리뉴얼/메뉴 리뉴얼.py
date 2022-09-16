from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    tmp = list()
    
    for num in course:
        tmp = []
        for order in orders:
            # if num > len(order):
            #   continue
              
            combination = combinations(order, num)
          
            for c in combination:
                # print(c)
                c = "".join(sorted(list(c)))
                tmp.append(c)
       

        
        counter = Counter(tmp).most_common()

        if len(counter) == 0:
          continue
        max_cnt = counter[0][1]
        if max_cnt > 1:
            for value, cnt in counter:
                if cnt == max_cnt:
                    answer.append(value)
    
    return sorted(answer)
