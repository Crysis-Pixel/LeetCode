class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] + nums[j]) == target:
                    if(i==j): continue
                    result.append(i)
                    result.append(j)
                    print(result)
                    return result
        return result

sol = Solution()

print(sol.twoSum([1,2,4], 6))
