class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letters = []
        nums = []
        for log in logs:
            if log[log.index(' ')+1].isdigit():
                nums.append(log)
            else:
                letters.append(log)
                
        return sorted(letters, key=lambda x:(x[x.index(' ')+1:], x[:x.index(' ')])) + nums
