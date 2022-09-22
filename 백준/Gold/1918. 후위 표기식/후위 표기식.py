import sys
from collections import deque

input = sys.stdin.readline

prior_operators = ("*", "/")

infix = deque(list(input().strip()))
tmp = []
priority_dict = dict()

priority = 0

while infix:
  symbol = infix.popleft()

  if symbol.isalpha():
    print(symbol, end="")

  else:
    if symbol == "(":
      priority += 1
    elif symbol == ")":
      if priority in priority_dict:
        while priority_dict[priority]:
          print(priority_dict[priority].pop(), end="")
        
      priority -= 1

    elif symbol in prior_operators:
      if priority not in priority_dict:
        priority_dict[priority] = [symbol]
      else:
        if len(priority_dict[priority]) > 0:
          # if priority_dict[priority][-1] in prior_operators:
          
          if priority_dict[priority][-1] in prior_operators:
            print(priority_dict[priority].pop(), end="")
        priority_dict[priority].append(symbol)

    else:
      if priority not in priority_dict:
        priority_dict[priority] = [symbol]

      else:
        if len(priority_dict[priority]) > 0:
          # if priority_dict[priority][-1] in prior_operators:
          
          while priority_dict[priority]:
            print(priority_dict[priority].pop(), end="")
        priority_dict[priority].append(symbol)

if priority in priority_dict:
  while priority_dict[priority]:
    print(priority_dict[priority].pop(), end="")