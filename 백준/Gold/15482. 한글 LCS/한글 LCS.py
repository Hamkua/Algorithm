import sys
input = sys.stdin.readline 

a = input().strip()
b = input().strip()


def make_data(s1, s2):
  data = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
  for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
      if(s1[i - 1] == s2[j - 1]):
        data[i][j] = data[i - 1][j - 1] + 1
      else:
        data[i][j] = max(data[i - 1][j], data[i][j - 1])

  return data

def calculate_lcs(s1, s2, data):
  result = ""
  x, y = len(s1), len(s2)
  while(x > 0 and y > 0):
    if(data[x][y] == data[x - 1][y]):
      x -= 1
    elif(data[x][y] == data[x][y - 1]):
      y -= 1
    else:
      result = s1[x - 1] + result
      x -= 1
      y -= 1

  return result   
  
print(len(calculate_lcs(a, b, make_data(a, b))))