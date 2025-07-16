# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n = len(bills)
        bill_5, bill_10 = 0, 0

        for bill in bills:
            if bill == 5:
                bill_5 +=1
            elif bill == 10:
                if bill_5 > 0:
                    bill_10 +=1
                    bill_5 -=1
                else:
                    return False
            else:
                if bill_10 > 0 and bill_5 > 0:
                    bill_5 -=1
                    bill_10 -=1
                elif bill_10 == 0 and bill_5 > 2:
                    bill_5 -= 3
                else:
                    return False
        return True

        