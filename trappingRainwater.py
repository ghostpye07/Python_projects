class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        left=[0]*n
        right=[0]*n
        maxi=-876543
        for i in range(0,n):
            left[i]=max(maxi,height[i])
            maxi=left[i]
        maxi=-876543
        for i in range(n-1,-1,-1):
            right[i]=max(maxi,height[i])
            maxi=right[i]
        ans=0
        for i in range(0,n):
            ans+=min(left[i],right[i])-height[i]
        return ans
