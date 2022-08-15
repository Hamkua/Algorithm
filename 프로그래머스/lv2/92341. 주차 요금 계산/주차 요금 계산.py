def solution(fees, records):
    answer = []
    dictionary = dict()
    info = dict()
    
    for record in records:
        record_info = record.split()

        time = record_info[0].split(":")
        hour = int(time[0])
        min = int(time[1])

        num = record_info[1]
        detail = record_info[2]

    
        if(detail == "IN"):
            dictionary[num] = hour * 60 + min

        elif(detail == "OUT"):
            dictionary[num] = hour * 60 + min - dictionary[num]
            tmp = dictionary.pop(num)

        
            if num not in info:
                info[num] = tmp
            else:
                info[num] += tmp

    for key in dictionary.keys():
        if key in info:
            info[key] += 23 * 60 + 59 - dictionary[key]
        else:
            info[key] = 23 * 60 + 59 - dictionary[key]


    key_set = sorted(list(info.keys()))

    for key in key_set:
        result = fees[1]
        time_diff = info[key]
        time_diff -= fees[0]
        if(time_diff > 0):
            if(time_diff // fees[2] > 0):
                result += fees[3] * (time_diff // fees[2])

            if(time_diff % fees[2] > 0):
                result += fees[3]

        answer.append(result)


    
    return answer