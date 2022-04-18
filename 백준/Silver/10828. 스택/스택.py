import sys 
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.link = None
        self.value = None

def push(item):
  global top
  newNode = Stack()
  newNode.value = int(item)
  newNode.link = top
  top = newNode

def pop():
  global top
  if(empty()):
    return -1
  result = top.value
  top = top.link
  return result
  

def size():
  global top
  size = 0
  tmp = top
  while(tmp.value != None):
    size += 1
    tmp = tmp.link
  return size

def empty():
  global top
  if(top.value == None):
    return 1
  else:
    return 0

def stack_top():
  global top
  if(top.value != None):
    return top.value
  else:
    return -1
    
top = Stack()
n = int(input().rstrip())
command = list()

result = list()
for i in range(n):
    command = input().strip().split()
    if(len(command)>1):
        push(command[1])
    elif(command[0] == "pop"):
        print(pop())
    elif(command[0] == "size"):
        print(size())
    elif(command[0] == "empty"):
        print(empty())  
    elif(command[0] == "top"):
        print(stack_top())
