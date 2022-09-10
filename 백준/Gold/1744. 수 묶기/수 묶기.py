import sys 
input = sys.stdin.readline 

n = int(input())

p =[]
m = []
result =0

for _ in range(n):
  a = int(input())
  if a == 1:
    result += 1
  elif a > 0:
    p.append(a)
  if a <= 0:
    m.append(a)

p.sort(reverse=True)
m.sort()

p_even = len(p)//2
if len(p)>=2:
  for i in range(p_even):
    result += p[i*2]*p[(i*2)+1]

m_even = len(m)//2
if len(m)>=2:
  for i in range(m_even):
    result += m[i*2]*m[(i*2)+1]

p_odd = len(p)%2
m_odd = len(m)%2

if m_odd!=0 and p_odd!=0:
  result += m[len(m)-1]+p[len(p)-1]

elif m_odd!=0:
  result += m[len(m)-1]
elif p_odd!=0:
  result += p[len(p)-1]

print(result)