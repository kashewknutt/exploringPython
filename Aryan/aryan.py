class Solution(object):
    def twoSum(self, nums, target):
        nums.sort()
        max_index = 0
        while max_index < len(nums) and nums[max_index] <= target:
            max_index += 1
        max_index -= 1
        print("max index: ", max_index)
        p = 0

        while p <= max_index:
            print("p: ",p)
            q = max_index
            while q >= p + 1:
                print("q: ",q)
                if nums[q] == (target - nums[p]):
                    return p, q
                q -= 1
            p += 1
        return None
    
    def bettertwoSum(self, nums, target):
        for i in range(len(nums)):
            print("i: ", i)
            for j in range(len(nums)):
                print("j: ", j)
                if i != j:
                    print("nums[i]: ", nums[i], "nums[j]: ", nums[j], "nums[i] + nums[j]: ", nums[i] + nums[j])
                    if nums[i] + nums[j] == target:
                        return i, j
        return None

solution = Solution()
nums = [3, 2, 4]

indices = solution.bettertwoSum(nums, 6)
if indices is None:
    print("No match found")
else:
    print("The indices are:", indices)