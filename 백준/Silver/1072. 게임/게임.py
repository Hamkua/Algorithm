import sys
input = sys.stdin.readline
x, y = map(int, input().strip().split())

left = 1
right = x
p = int(y * 100 / float(x))
# print(p)

if p >= 99 :
  print(-1)
else:
  while(left <= right):
    
    mid = (left + right) // 2
    new_p = int((y + mid  )* 100 / float(x + mid))
    # print(mid,new_p, left, right)
    
    if new_p > p:
      
      right = mid - 1
    else:

      left = mid + 1

  # print("dwanldawl")
  print(left)
