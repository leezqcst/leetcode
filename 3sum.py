class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i = 0
        result = []

        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == - nums[i]:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                else:
                    if nums[j] + nums[k] < -nums[i]:
                        j += 1
                    else:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1
        return result

if __name__ == '__main__':
    print Solution().threeSum([0,0,0,0])