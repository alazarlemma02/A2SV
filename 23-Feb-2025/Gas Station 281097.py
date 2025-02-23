# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        current_gas_balance = 0
        starting_station = 0
        for i in range(len(gas)):
            current_gas_balance += gas[i] - cost[i]

            if current_gas_balance < 0:
                current_gas_balance = 0
                starting_station = i + 1
        
        return starting_station


        