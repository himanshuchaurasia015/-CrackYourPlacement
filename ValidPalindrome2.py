class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        count1=0
        while i<j :
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                count1+=1
                if count1>1:
                    break
                i+=1
            
        i=0
        j=len(s)-1
        count2=0
        while i<j :
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                count2+=1
                if count2>1:
                    break
                j-=1
        if (count1==1 or count2 ==1) or (count1==0 or count2==0):
            return  True
        return False
          

            

        
            
        
        


        
        

        