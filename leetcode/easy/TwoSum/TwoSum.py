class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        for i in range(len(nums)-1) :
            for j in range(i + 1, len(nums)) :
                if nums[i] + nums[j] == target :
                    return [i, j]
        
        return []
    

sol1 = Solution()
sol2 = Solution()
sol3 = Solution()

print(sol1.twoSum([2,7,11,15], 9))
print(sol2.twoSum([3, 2, 4], 6))
print(sol3.twoSum([3, 3], 6))
