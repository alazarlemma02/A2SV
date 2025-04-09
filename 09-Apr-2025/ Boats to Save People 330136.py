# Problem:  Boats to Save People - https://leetcode.com/problems/boats-to-save-people/description/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        min_boats = 0
        left, right = 0, n-1
        people.sort()
        while left <= right:
            curr = limit-people[right]
            right -=1
            min_boats +=1
            if left <= right and curr >= people[left]:
                left +=1
        return min_boats

            


            
            


            
            

        