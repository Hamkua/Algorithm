import sys
input = sys.stdin.readline

data = input().strip()
boom = input().strip()
length = len(boom)

tmp = []

# while(boom in data):
#   index = data.find(boom)
#   data = data[:index] + data[index + length:]

for char in data:
  tmp.append(char)
  if(char == boom[-1] and ''.join(tmp[-length:]) == boom):
    del tmp[-length:]

result = ''.join(tmp)
    
print("FRULA" if len(result) == 0 else result)