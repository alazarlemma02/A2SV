# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()

        prev_sum = skill[0] + skill[n-1]
        if n <= 2:
            return skill[0] * skill[n-1]

        left, right, skill_map = 1, n-2, defaultdict(int)
        skill_map[skill[0]] = skill[0] * skill[n-1]

        while left <= right:
            if skill[left] + skill[right] != prev_sum:
                return -1
            skill_map[skill[left]] += skill[left] * skill[right]
            left +=1
            right -=1
        
        return sum(skill_map.values())
            