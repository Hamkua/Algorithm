from collections import deque

def check(p):
    queue = deque()
    if(p == ""):
        return True
 
    
    for i in p:
        if(i == "("):
            queue.append("(")
      
        else:
            if(len(queue) == 0):
                return False
            pop = queue.popleft()
    return True
        
def solution(p):
    answer = ''
    
    if(check(p)):
        return p

    balanceScore = 0
    balanceIndex = 0
    for i in range(len(p)):
        if(p[i] == "("):
            balanceScore+=1
        else:
            balanceScore-=1
        if(balanceScore == 0):
            balanceIndex = i
            break

    u = p[:balanceIndex+1]
    v = p[balanceIndex+1:]

    if(check(u)):
        return  u + solution(v)

    else:
        r = "(" + solution(v) + ")"
        
        u = u[1:-1]
        for i in u:
            if i == ")":
                r += "("
            else:
                r += ")"
        return r