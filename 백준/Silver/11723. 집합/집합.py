import sys
input = sys.stdin.readline

n = int(input())
s = set()

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다. 
reset = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in range(n):
  command = list(input().strip().split())
  if(len(command) == 1):
    cmd = command[0]
    if(cmd == "all"):
      s = set(reset)
    elif(cmd == "empty"):
      s.clear()

  else:
    cmd, num = command[0], int(command[1])
    
    if(cmd == "add"):
      s.add(num)
    
    elif(cmd == "remove"):
      s.discard(num)
   
    elif(cmd == "check"):
      if num in s:
        print(1)
      else:
        print(0)
  
    elif(cmd == "toggle"):
      if num in s:
        s.discard(num)
      else:
        s.add(num)
