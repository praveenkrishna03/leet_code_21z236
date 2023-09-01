class Solution(object):
    def twoSum(self, nums, target):
        length=len(nums)
        out=[]
        for x in range(length):
            for y in range(x+1,length):
                if nums[x]+nums[y] == target:
                    out.append(x)
                    out.append(y)
        return out