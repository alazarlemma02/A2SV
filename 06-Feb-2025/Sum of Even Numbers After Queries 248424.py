# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []

        even_sum = 0
        for num in nums:
            if num % 2 == 0:
                even_sum += num

        for query in queries:
            current_num = nums[query[1]]
            if current_num % 2 ==0:
                even_sum -= current_num
            nums[query[1]] += query[0]
            if nums[query[1]] % 2 ==0:
                even_sum += nums[query[1]]

            answer.append(even_sum)
        
        return answer   
            

        