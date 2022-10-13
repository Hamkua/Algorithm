def solution(s):
    answer = 0

    if len(s) < 2 and s == s[::-1]:
        return len(s)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    def expand(left, right):
        while(0 <= left and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
            
        return len(s[left + 1:right])
    

    for i in range(len(s) - 1):
        answer = max(answer, expand(i, i + 1), expand(i, i + 2))
        
        
        
        
        
    return answer