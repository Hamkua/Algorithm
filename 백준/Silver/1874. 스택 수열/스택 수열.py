import sys
input = sys.stdin.readline

n = int(input())

stack = list()
result = list()
is_stack_true = True
cnt = 1
for i in range(n):
  num = int(input())
  while(cnt <= num):
    stack.append(cnt)
    cnt += 1
    result.append("+")

  if num == stack[-1]:
    stack.pop()
    result.append("-")
  else:
    is_stack_true = False 
    
if is_stack_true == False:
  print("NO")
else:
  for r in result:
    print(r)