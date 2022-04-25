import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    #n = 문서의 개수 , m= 궁금한 순서
    n, m = map(int, input().strip().split())
    data = list(map(int, input().strip().split()))
    tmp = [0 for _ in range(n)]
    tmp[m] = 1
    cnt = 0
    while(1):
        if data[0] == max(data):
            cnt += 1
            if tmp[0] == 1:
                print(cnt)
                break
            else:
                del tmp[0]
                del data[0]
        else:
            data.append(data[0])
            del data[0]
            tmp.append(tmp[0])
            del tmp[0]       