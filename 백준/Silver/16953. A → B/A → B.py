from collections import deque
import sys

input = sys.stdin.readline

def cal_1(curr_num):
  num = 2*curr_num
  return num

def cal_2(curr_num):
  num = curr_num*10 + 1
  return num

a,b = map(int, input().split())
queue = deque()
cnt = 1

queue.append((a,cnt))
can_cal = False

while queue:
  curr_num, count = queue.popleft()

  if curr_num > b:
    continue

  if curr_num == b:
    print(count)
    can_cal = True
    break

  temp = cal_1(curr_num)
  queue.append((temp, count+1))
  
  temp = cal_2(curr_num)
  queue.append((temp, count+1))

if can_cal == False:
  print(-1)