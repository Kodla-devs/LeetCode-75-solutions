class Solution(object):
    def removeStars(self, s):
        cnt = 0 
        k = [] 

        for char in reversed(s):
            if char == '*':
                cnt += 1
            else:
                if cnt > 0:
                    cnt -= 1 
                else:
                    k.append(char) 
                    
        return ''.join(reversed(k))
        