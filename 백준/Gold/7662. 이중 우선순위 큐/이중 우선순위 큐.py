import heapq
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

  minq = []
  maxq = []
  done = dict()
  
  n = int(input())
  for i in range(n):
    a,b = input().strip().split()
    b = int(b)
    if(a == "I"):
      if b in done:
        done[b] += 1

      else:
        done[b] = 1
        if b >= 0:
          heapq.heappush(maxq, -1 * b)
        else:
          heapq.heappush(minq, b)


    elif(a == "D"):
      if not maxq and not minq:
        continue
        
      if( b == -1):
        if minq:
          minq.sort()
          minv = minq[0]
          if done[minv] > 1:
            done[minv] -= 1
  
          else:
            done.pop(minv)
            heapq.heappop(minq)
        elif maxq:
          maxq.sort()
          minv = -1 * maxq[-1]
          if done[minv] > 1:
            done[minv] -= 1
  
          else:
            done.pop(minv)
            maxq.pop()
        else:
          continue
          
      elif( b == 1):
        if maxq:
          maxq.sort()
          maxv = -maxq[0]
          if done[maxv] > 1:
            done[maxv] -= 1
  
          else:
            done.pop(maxv)
            heapq.heappop(maxq)

        elif minq:
          minq.sort()
          maxv = minq[-1]
          if done[maxv] > 1:
            done[maxv] -= 1
  
          else:
            done.pop(maxv)
            minq.pop()

        else:
          continue

 
    
  if maxq and minq:
    minq.sort()
    maxq.sort()
    print(-maxq[0], minq[0])

  elif maxq:
    maxq.sort()
    print(-maxq[0], -maxq[-1])

  elif minq:
    minq.sort()
    print(minq[-1], minq[0])

  else:
    print("EMPTY")