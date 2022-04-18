import sys
input = sys.stdin.readline

class QNode:
    def __init__(self):
        self.value = None
        self.link = None

class LQueueType:
    def __init__(self):
        self.front = None
        self.rear = None 

def push(number):
    global LQ
    newNode = QNode()
    newNode.value = number
    
    if(empty()):
        LQ.front = newNode
        LQ.rear = newNode
    else:
        LQ.rear.link = newNode 
        LQ.rear = newNode
    

def pop():
    global LQ
    if(empty()):
        return -1
    result = LQ.front.value
    LQ.front = LQ.front.link
    return result

def size():
    global LQ
    result = 0
    tmp = LQ.front
    while(tmp != None):
        result += 1
        tmp = tmp.link
    return result

def empty():
    global LQ
    if(LQ.front == None):
        return 1
    return 0

def front():
    global LQ
    if(empty()):
        return -1
    return LQ.front.value

def back():
    global LQ
    if(empty()):
        return -1
    return LQ.rear.value

n = int(input().rstrip())
LQ = LQueueType()
for i in range(n):
    command_list = input().strip().split()
    if(len(command_list) > 1):
        push(int(command_list[1]))
    elif(command_list[0] == 'pop'):
        print(pop())
    elif(command_list[0] == 'size'):
        print(size())
    elif(command_list[0] == 'empty'):
        print(empty())
    elif(command_list[0] == 'front'):
        print(front())
    else:
        print(back())