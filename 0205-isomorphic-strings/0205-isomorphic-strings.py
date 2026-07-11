class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            d1={}
            d2={}
            for i in range(0,len(s)):
                if s[i] not in d1:
                    d1[s[i]]=str(i)
                else:
                    d1[s[i]]+=str(i)
                    
                if t[i] not in d2:
                    d2[t[i]]=str(i)
                else:
                    d2[t[i]]+=str(i)
            if list(d1.values())==list(d2.values()):
                return True
            else:
                return False
            
        