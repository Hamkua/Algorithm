def solution(n, lost, reserve):
    answer = 0
    dx = [-1, 1]

    intersection = set(reserve) & set(lost)
    reserve = list(set(reserve) - intersection)
    lost = list(set(lost) - intersection)

    reserve.sort()
    for i in range(len(reserve)):
        for j in range(2):
            nx = reserve[i] + dx[j]
            if(0<nx<=n):
                if nx in lost:
                    lost.remove(nx)
                    break
                    
    answer = n - len(lost)
    
    return answer

#  int n = 5;
#     int[] lost = {1, 2, 4};
#     int[] reserve = {2, 4, 5}; // 정답 4

#     int n = 5;
#     int[] lost = {1, 2, 4};
#     int[] reserve = {2, 3, 4, 5}; // 정답 4