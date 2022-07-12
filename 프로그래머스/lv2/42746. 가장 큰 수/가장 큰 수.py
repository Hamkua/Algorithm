from functools import cmp_to_key
def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0
            
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = cmp_to_key(compare))
    
    answer = "".join(numbers)
    answer = answer.lstrip("0")
    if(answer == ""):
        answer += "0"
    return answer