import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

class Tree:
  def __init__(self, value = None, left = None, right = None, parent = None):
    self.parent = parent
    self.value = value
    self.left = left
    self.right = right

def search(tree):
  if tree.left != None:
    search(tree.left)

  if tree.right != None:
    search(tree.right)
    
  print(tree.value)
  

data = []

while(1):
  try:
    n = int(input().strip())
    data.append(n)
  except:
    root = Tree(value = data[0])
    tmp = root
    
    for i in range(1,len(data)):
      
      if(tmp.value > data[i]):
        left_child = Tree(value = data[i], parent = tmp)
        tmp.left = left_child
        tmp = tmp.left
      

      else:
        right_child = Tree(data[i])
        root_tmp = root    
        while(root_tmp != None):
          if(root_tmp.value < right_child.value):
            if(root_tmp.right != None):
              root_tmp = root_tmp.right
            else:
              root_tmp.right = right_child
              break
            

          else:
            if(root_tmp.left != None):
              root_tmp = root_tmp.left
            else:
              root_tmp.left = right_child
              break
        # if(root_tmp == None):
        #   root_tmp.parent.right = right_child
  
    search(root)
    break
