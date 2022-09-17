from itertools import combinations
# from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    answer = []
    # dictionary = defaultdict(list)
    dictionary = dict()

    for info_list in info:
        info_list = info_list.split()
        score = int(info_list[-1])
        info_list = info_list[:-1]
        
        for i in range(5):
            
            combination_list = list(combinations(info_list, i))
            for combination in combination_list:
                
                key = "".join(combination)
                if key not in dictionary:
                    dictionary[key] = ([score])
                else:
                    dictionary[key].append(score)
                
                
        

        # print(dictionary)

    for key in dictionary.keys():
        dictionary[key].sort()
        
    for requirement in query:
        requirement = [i for i in requirement.split() if i != "and" and i != "-"]
        # print(requirement)
        score = int(requirement[-1])
        
        requirement = "".join(requirement[:-1])
        if requirement not in dictionary:
            answer.append(0)
            continue
            
        result = dictionary[requirement]
        
        idx = bisect_left(result, score)
        answer.append(len(result) - idx)
        
    return answer