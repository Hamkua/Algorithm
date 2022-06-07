import sys

input = sys.stdin.readline
def preorder(x):
  global preorder_result

  preorder_result += chr(65 + x)
  
  if tree[x][0] != -1:
    preorder(tree[x][0])

  if tree[x][1] != -1:
    preorder(tree[x][1])

  
def inorder(x):
  global inorder_result
  
  if tree[x][0] != -1:
    inorder(tree[x][0])
    
  inorder_result += chr(65 + x)

  if tree[x][1] != -1:
    inorder(tree[x][1])

def postorder(x):
  global postorder_result
  
  if tree[x][0] != -1:
    postorder(tree[x][0])

  if tree[x][1] != -1:
    postorder(tree[x][1])

  postorder_result += chr(65 + x)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n):
  tmp = list(input().strip().split())
  index = ord(tmp[0]) - 65
  for j in range(1,len(tmp)):
    if tmp[j] == ".":
      tree[index].append(-1)
      continue
    tree[index].append(ord(tmp[j]) - 65)
  
preorder_result = ""
inorder_result = ""
postorder_result = ""

preorder(0)
inorder(0)
postorder(0)

print(preorder_result)
print(inorder_result)
print(postorder_result)
