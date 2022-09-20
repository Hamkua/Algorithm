from bisect import bisect_left
from itertools import combinations


def solution(info, query):
    answer = []
    dictionary = dict()
    
    for programmer_info in info:
        programmer_info = programmer_info.split()
        score = int(programmer_info.pop())
        for i in range(5):
            combination_list = combinations(programmer_info, i)
            for combination in combination_list:
                key = "".join(combination)
                if key not in dictionary:
                    dictionary[key] = [score]
                else:
                    dictionary[key].append(score)
    

    for key in dictionary.keys():
        dictionary[key].sort()

    for requirement in query:
        requirement = requirement.replace("and", "")
        requirement = requirement.replace("-", "")
        requirement = requirement.split()
    
        score = int(requirement.pop())
    
        key = "".join(requirement)
    

        if key not in dictionary:
            answer.append(0)
        else:
            answer.append(len(dictionary[key]) - bisect_left(dictionary[key], score))
        
    return answer
    