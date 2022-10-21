import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,cnt):
  global result
  result = max(result,cnt)
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<r and 0<=ny<c and data[nx][ny] not in abc:
      
      abc.add(data[nx][ny])
      dfs(nx,ny,cnt+1)    #재귀적으로 반복,
      abc.remove(data[nx][ny])    #재귀가 끝나고 다시 돌아왔을 때, 다른 경로로 갈 수 있으니 remove로 위치를 지워줌.

result = 0
abc = set()
r, c = map(int, input().split())

data = []
for _ in range(r):
  data.append(list(input().rstrip()))

abc.add(data[0][0])    #빈 집합에 처음 위치를 추가한다.
dfs(0,0,1)    #처음 위치도 이동거리 1로 계산하므로, 1을 dfs함수의 인수로 전달
print(result)    