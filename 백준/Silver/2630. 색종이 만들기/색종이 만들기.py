import sys
input = sys.stdin.readline

graph = []

def get_cnt(x,y,n):
  global white, blue
  tmp = graph[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      div_index = n//2
      if(graph[i][j] != tmp):
        get_cnt(x,y,div_index)
        get_cnt(x,y+div_index,div_index)
        get_cnt(x+div_index, y, div_index)
        get_cnt(x+div_index, y+div_index, div_index)
        return

  if(tmp == 0):
    white += 1
    return

  else:
    blue += 1
    return
            
blue = 0
white = 0

n = int(input())
for _ in range(n):
  graph.append(list(map(int, input().strip().split())))

get_cnt(0,0,n)
print(white)
print(blue)
          
      
      