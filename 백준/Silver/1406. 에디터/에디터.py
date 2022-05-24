import sys
input = sys.stdin.readline

string = list(input().strip())
stack = []
m = int(input().strip())

for _ in range(m):
  cmd = list(input().strip().split())
  if(len(cmd) >= 2):
    string.append(cmd[1])

  else:
    if(cmd[0] == "L"):
      if string:
        stack.append(string.pop())
   
    elif(cmd[0] == "D"):
      if stack:
        string.append(stack.pop())

    elif(cmd[0] == "B"):
      if string:
        string.pop()

string += reversed(stack)
print("".join(string))