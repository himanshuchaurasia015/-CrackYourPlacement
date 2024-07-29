class Solution:
    def maxArea(self, height):
        maxarea=0
        area=0
        i=0
        j=len(height)-1
        while(i<j):
            area=min(height[j],height[i])*(j-i)
            maxarea=(max(area,maxarea))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
            
        return maxarea
