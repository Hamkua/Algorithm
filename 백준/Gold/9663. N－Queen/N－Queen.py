import sys
input = sys.stdin.readline 

n = int(input())
data = [0] * n

result = 0

def check(x):
  for qx in range(x):
    qy = data[qx]
    if qx == x or qy == data[x] or abs(x - qx) == abs(data[x] - qy):
      return False

  return True 


def backtracking(idx):
  global result

  if idx == n:
    # for i in range(n):
    #   print("({}, {})".format(i, data[i]), end="\t")
    # print()
    result += 1
    return 
    
  else:
    for i in range(n):
      data[idx] = i
      if check(idx):
        backtracking(idx + 1)
          
backtracking(0)
print(result)