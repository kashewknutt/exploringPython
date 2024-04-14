class Solution(object):
    def twoSum(self, nums, target):
        hashmap={}
        for i in range(len(nums)):
            if target-nums[i] in hashmap:
                return i,hashmap[target-nums[i]]
            else:
                hashmap[nums[i]]=i


solution = Solution()
nums = [-3,4,3,90]

indices = solution.twoSum(nums, 0)
if indices is None:
    print("No match found")
else:
    print("The indices are:", indices)