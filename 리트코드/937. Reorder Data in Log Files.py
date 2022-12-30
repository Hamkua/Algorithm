class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        strings = []
        
        for log in logs:
            is_string = False
            for x in log.split()[1:]:
                if x.isdigit() == False:
                    strings.append(log)
                    is_string = True
                    break
            
            if(is_string == False):
                digits.append(log)


        
        strings.sort(key = lambda x : (x.split()[1:], x.split()[0]))

        return strings + digits