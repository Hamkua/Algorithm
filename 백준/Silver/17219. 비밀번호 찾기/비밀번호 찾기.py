import sys
input = sys.stdin.readline 

n, m = map(int, input().strip().split())
dictionary = dict()

for _ in range(n):
  k, v = input().strip().split()
  dictionary[k] = v

for _ in range(m):
  print(dictionary[input().strip()])