import sys
input = sys.stdin.readline

def remove_node(x):
  for i in tree[x]:
    remove_node(i)
  tree[x].append(-1)

n = int(input())
data = list(map(int, input().strip().split()))
tree = [[] for _ in range(n + 1)]
r = int(input())
result = 0

for i in range(n):
  if(data[i] == -1):
    continue
 
  tree[data[i]].append(i)
remove_node(r)

for i in range(n):
  if r in tree[i]:
    tree[i].remove(r)
  if(len(tree[i]) == 0):
    result += 1

print(result)