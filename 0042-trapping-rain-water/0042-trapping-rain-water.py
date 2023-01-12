class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        lmax = height[l]
        rmax = height[r]
        water = 0
        while l<r:
            if lmax < rmax:
                l += 1
                lmax = max(height[l], lmax)
                water += lmax - height[l]
                
            else:
                r -= 1
                rmax = max(height[r], rmax)
                water += rmax - height[r]
                
        return water