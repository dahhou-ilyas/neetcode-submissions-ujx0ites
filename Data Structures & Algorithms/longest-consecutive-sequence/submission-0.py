class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_sequence = 0
        count_current_sequence = 0
        numberSet = set(nums)

        for num in nums:
            current_number = num
            prev = current_number - 1
            if prev not in numberSet :
                while current_number in numberSet :
                    count_current_sequence += 1
                    current_number = current_number + 1
            max_sequence = max(max_sequence,count_current_sequence)
            count_current_sequence = 0

        return max_sequence
        