s = input()

data = []
for i in range(len(s)):
  data.append(s[i:])

data.sort(key=lambda x: (x))
for d in data:
  print(d)