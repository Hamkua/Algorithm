def solution(number, k):
    answer = ''
    tmp = []
    tmp.append(number[0])
    index = 1
    
    for i in range(index, len(number)):
        while(k > 0):
            if(len(tmp) > 0 and tmp[-1] < number[i]):
                tmp.pop()
                k -= 1
            else:
                break
        tmp.append(number[i])
        # print("index = {} , {}".format(i,tmp))
    
    tmp = tmp[:len(tmp) - k]
    answer = "".join(tmp)
    return answer