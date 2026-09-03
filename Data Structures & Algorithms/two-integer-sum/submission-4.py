class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]]= i
        for i in range(len(nums)):

            n_target = target - nums[i]


            if n_target in hashmap and hashmap[n_target] != i:
                return [i, hashmap[n_target]]