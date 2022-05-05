import sys
input = sys.stdin.readline

n = int(input())


def get_cnt(x,y,n):
  global color1, color2, color3
  div_index = n//3
  tmp = graph[x][y]
  for i in range(x,x+n):
    for j in range(y,y+n):
      if(tmp != graph[i][j]):
        get_cnt(x,y,div_index)
        get_cnt(x+div_index, y, div_index)
        get_cnt(x+2*div_index, y, div_index)
        get_cnt(x, y+div_index, div_index)
        get_cnt(x, y+2*div_index, div_index)
        get_cnt(x+div_index, y+div_index, div_index)
        get_cnt(x+div_index, y+2*div_index, div_index)
        get_cnt(x+2*div_index, y+div_index, div_index)
        get_cnt(x+2*div_index, y+2*div_index,div_index)
        return

  if(tmp == -1):
    color1 += 1

  elif(tmp == 0):
    color2 += 1

  else:
    color3 += 1
  
color1 = 0
color2 = 0 
color3 = 0
graph = []
for _ in range(n):
  graph.append(list(map(int, input().strip().split())))

get_cnt(0,0,n)
print(color1)
print(color2)
print(color3)