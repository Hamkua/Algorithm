def solution(arr):
    answer = []
    for num in arr:
        if len(answer) < 1:
            answer.append(num)
        else:
            if answer[-1] != num:
                answer.append(num)
    return answer