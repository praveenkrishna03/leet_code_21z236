class Solution(object):
    def lengthOfLongestSubstring(self, s):
        length=len(s)
    
        counts = [0] * length
        if(length==0):
            maxi=0
        else:
            for i in range (length):
                temp=[]
                temp.append(s[i])
                counts[i]=1
                for j in range(i+1,length):
                    if(s[j] in temp):
                        break
                    else:
                        temp.append(s[j])
                        counts[i]+=1
            maxi = max(counts)     
        
        
        return maxi