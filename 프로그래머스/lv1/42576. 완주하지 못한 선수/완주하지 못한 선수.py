def solution(participant, completion):
    answer = ''
    dictionary = dict()
    for p in participant:
        if p in dictionary:
            dictionary[p] += 1
        else:
            dictionary[p] = 1

    for c in completion:
        dictionary[c] -= 1

    for k, v in dictionary.items():
        if v > 0:
            answer = k
    return answer