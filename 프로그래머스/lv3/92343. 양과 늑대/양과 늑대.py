def solution(info, edges):
    answer = 0
    data = [[] for _ in range(len(info))]

    for x, y in edges:
        data[x].append(y)
    
    result = []

    def dfs(current_index, sheep, wolf, next_index_list):
        result.append(sheep)
        if current_index in next_index_list:
            next_index_list.remove(current_index)


        for next_index in next_index_list:
            if info[next_index] == 0:
                dfs(next_index, sheep + 1, wolf, next_index_list + data[next_index])

            elif info[next_index] == 1:
                if((sheep - wolf) <= 1):
                    continue
                dfs(next_index, sheep, wolf + 1, next_index_list + data[next_index])


    dfs(0,1,0, data[0])
    result.sort()
    answer = result.pop()
    return answer