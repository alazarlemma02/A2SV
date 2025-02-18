# Problem: Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/description/?envType=problem-list-v2&envId=array

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        max_distance = 0
        start = [0, 0]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        dir = 0
        obstacles = { tuple(obs) for obs in obstacles }
        for com in commands:
            if com == -1 :
                dir = (dir + 1) % 4
            elif com == -2:
                dir = (dir - 1) % 4
            else:
                curr = directions[dir]
                for _ in range(com):
                    next_position = (start[0] + curr[0], start[1] + curr[1]) 
                    if next_position in obstacles:
                        break
                    start[0], start[1]= next_position
                distance = pow(start[0], 2) + pow(start[1], 2)
                max_distance = max(distance, max_distance)
        return max_distance
        
                

        