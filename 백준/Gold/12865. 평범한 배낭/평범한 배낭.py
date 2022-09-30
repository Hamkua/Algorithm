import sys
input = sys.stdin.readline

n, m =map(int, input().strip().split())

data = [[0] * (m + 1) for _ in range(n + 1)]
w_list = list()
v_list = list()

wv_dict = dict()
for i in range(1,n + 1):
  w, v = map(int, input().strip().split())

  
  for j in range(1, m + 1):
    if j - w >= 0:
      data[i][j] = max(data[i - 1][j], v + data[i - 1][j - w])

    else:
      data[i][j] =data[i - 1][j]

print(data[-1][-1])
