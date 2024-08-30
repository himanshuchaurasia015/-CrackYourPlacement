class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        path+="/"
        i=0
        j=1
        res="/"
        while(j<len(path)):
            if path[i]=="/" and path[j]=="/" :
                if i+1==j:
                    i=j
                else:
                    p=path[i+1:j]
                    if p==".." and stack:
                        stack.pop()
                    elif p!=".." and p!=".":
                        stack.append(p)
                    i=j
            j+=1
        res+="/".join(stack)
        return res


        