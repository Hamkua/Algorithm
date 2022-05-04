import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  cnt_zero = 1
  cnt_one = 0
  n = int(input())
  
  for i in range(n):
    if(i==0):
      cnt_zero = 0
      cnt_one = 1

    elif(i == 1):
      cnt_zero = 1
      cnt_one = 1

    else:
      tmp = cnt_one
      cnt_one += cnt_zero
      cnt_zero = tmp
      
  print("{} {}".format(cnt_zero, cnt_one))