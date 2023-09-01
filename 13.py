class Solution(object):
    def romanToInt(self, s):
        out=0
        for x in range(len(s)):    
            if(s[x]=='M'):
                if( x > 0 and s[x - 1] == 'C'):
                    out+=800 
                else:
                    out+=1000
                
            elif(s[x]=='D'):
                if(x  > 0 and s[x-1]=='C'):
                    out+=300
                else:
                    out+=500
            elif(s[x]=='C'):
                if(x  > 0 and s[x-1]=='X'):
                    out+=80    
                else:
                    out+=100
            elif(s[x]=='L'):
                if(x  > 0 and s[x-1]=='X'):
                    out+=30
                else:
                    out+=50
            elif(s[x]=='X'):
                if(x  > 0 and s[x-1]=='I'):
                    out+=8
                else:
                    out+=10
            elif(s[x]=='V'):
                if(x  > 0 and s[x-1]=='I'):
                    out+=3
                else:
                    out+=5
            elif(s[x]=='I'):
                out+=1
            
        return out
            
        