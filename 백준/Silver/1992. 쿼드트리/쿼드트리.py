import sys 
input = sys.stdin.readline

n = int(input())
data = []
result = []


def solution(x, y, cnt):
  check = True  
  
  if(cnt == 1):
    result.append(str(data[x][y]))
    return


  div_cnt = cnt // 2
  collation_value = data[x][y]


  for i in range(x, x + cnt):
    for j in range(y, y + cnt):
      
      tmp =[]
      if(collation_value != data[i][j]):
        result.append("(")
        tmp.clear()
        check = False
        
        for a in range(2):
          for b in range(2):
            solution(x + a * div_cnt, y + b * div_cnt, div_cnt)

        result.append(")")
        return
      

  if(check):
    result.append(str(collation_value))
    
for _ in range(n):
  data.append(list(map(int,input().strip())))

solution(0,0,n)
result = ''.join(result)
print(result)