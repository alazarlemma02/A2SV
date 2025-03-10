# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0: return 0
        
        nums = list(str(num))
        
        is_negative = nums[0] == "-"

        if is_negative:
            del nums[0]
        
        if is_negative:
            nums.sort(reverse=True)
        else:
            nums.sort()

        if not is_negative:
            zero_count = nums.count("0")
            res = nums[zero_count] + ("0" * zero_count)

            st = ""
            for i in range(zero_count+1, len(nums)):
                st += nums[i]
            
            return int(res + st)
            
        else:
            return int("".join(nums)) * (-1)
        
        
