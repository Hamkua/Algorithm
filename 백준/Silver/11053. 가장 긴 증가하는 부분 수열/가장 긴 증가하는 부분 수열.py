import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().strip().split()))

dictionary = dict()
for i in range(len(data)):
  if data[i] not in dictionary:
    dictionary[data[i]] = 1

  
  for j in range(len(data[:i + 1])):
    if data[j] < data[i]:
      dictionary[data[i]] = max(dictionary[data[j]] + 1, dictionary[data[i]])

print(max(dictionary.values()))