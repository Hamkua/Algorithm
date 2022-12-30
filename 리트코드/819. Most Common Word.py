from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        result = []
        for word in re.sub(r'[^\w]', ' ', paragraph).split():
            word = word.lower()
            if word not in banned:
                result.append(word)

        
        return Counter(result).most_common(1)[0][0]
        