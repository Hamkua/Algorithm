import sys 
input = sys.stdin.readline


t = int(input())
    
for _ in range(t):
  result = 1
  dictionary = dict()
  n = int(input())
  for i in range(n):
    a,b = input().strip().split()
    if b not in dictionary:
      dictionary[b] = [a]
    else:
      dictionary[b].append(a)

  key_set = dictionary.keys()
  for key in key_set:
    result *= (len(dictionary[key]) + 1)
      
  result -= 1
  print(result)