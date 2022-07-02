n, m = map(int,input().split())
floor = []
for _ in range(n):
    floor.append(list(input()))
result = 0
def dfs(x,y):
    if x>=n or x<0 or y >= m or y < 0:
        return False
    if floor[x][y] == '-':
        floor[x][y] = '*'
        dfs(x,y+1)
        return True
    return False

def dfs_(x,y):
    if x>=n or x<0:
        return False
    if floor[x][y] == '|':
        floor[x][y] = '*'
        dfs_(x+1,y)
        return True
    return False

for i in range(n):
    for j in range(m):
        if floor[i][j] == '-' and dfs(i, j) == True:
            result += 1
        if floor[i][j] == '|' and dfs_(i, j) == True:
            result += 1
print(result)

