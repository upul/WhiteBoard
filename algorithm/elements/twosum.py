class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        remains = {target-v:k for k, v in enumerate(nums)}
        for k, v in enumerate(nums):
            if v in remains and remains[v] != k:
                return [k, remains[v]]
        return []

if __name__ == '__main__':
    data = [3, 3]
    sol = Solution()
    print(sol.twoSum(data, 6))