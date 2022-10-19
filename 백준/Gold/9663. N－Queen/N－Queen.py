import sys
input = sys.stdin.readline 

n = int(input())
data = [0] * n

result = 0

#def check(x):
#  for qx in range(x):
#    qy = data[qx]
#    if qx == x or qy == data[x] or abs(x - qx) == abs(data[x] - qy):
#      return False

#  return True 

def check(x, y):
  for qx in range(x):
    qy = data[qx]
    if qx == x or qy == y or abs(x - qx) == abs(y - qy):
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
      isContinue = True
      data[idx] = i
      for qx in range(idx):
        qy = data[qx]
        if qx == idx or qy == data[idx] or abs(idx - qx) == abs(data[idx]- qy):
            isContinue = False
            break
        
      if isContinue:
        backtracking(idx + 1)
          
backtracking(0)
print(result)