def solution(number, k):
    #1. 스택 생성
    collected = []

    for (i, num) in enumerate(number):
        #2. 만약 collected이 num보다 작은 경우 and k > 0일 경우 
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        
        if k == 0:
            collected += number[i:]
            break

        collected.append(num)

    #만약 k가 0보다 크다면 collected를 뒤에서 k개 자름.
    collected = collected[:-k] if k > 0 else collected
    answer = "".join(collected)
    return answer