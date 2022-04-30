from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]

graph = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
def q(x,y,number):
    result = [0,0,0]
                          
    queue = deque()
    queue.append((x,y))
    
    tmp = [[0]*3 for _ in range(4)] 
    first_x, first_y = x, y
    
    while(queue):
        x,y = queue.popleft()
        if(graph[x][y] == number):
            result[0] = x 
            result[1] = y
            result[2] = tmp[x][y]
            return result
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if(0<=nx<4 and 0<=ny<3 and (nx!=first_x or ny!=first_y)):
                if(tmp[nx][ny] == 0):
                    queue.append((nx,ny))
                    tmp[nx][ny] = tmp[x][y] + 1                   
                
def solution(numbers, hand):
    answer = ''
    
    l_x, l_y = 3,0
    r_x, r_y = 3,2
    
    for n in numbers:
        
        if(n in [1,4,7]):
            for i in range(4):
                if(n == graph[i][0]):
                    l_y = 0
                    l_x = i
                    answer += 'L'
                    
        elif(n in [3,6,9]):
            for i in range(4):
                if(n == graph[i][2]):
                    r_y = 2 
                    r_x = i
                    answer += 'R'
        
        else:
            r_result = q(r_x, r_y, n)
            l_result = q(l_x, l_y, n)
        
            rcount = r_result[2]
            lcount = l_result[2]
            if(rcount > lcount):
                answer += 'L'
                l_x, l_y = l_result[0], l_result[1]
            elif(rcount < lcount):
                answer += 'R'
                r_x, r_y = r_result[0], r_result[1]
            else:
                if(hand == "right"):
                    answer += 'R'
                    r_x, r_y = r_result[0], r_result[1]
                else:
                    answer += 'L'
                    l_x, l_y = l_result[0], l_result[1]
    
    return answer