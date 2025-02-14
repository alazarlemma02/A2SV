# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:

    def __init__(self):
        self.frequency_tracker = defaultdict(int)
        self.num_fre_tracker = defaultdict(int)
        
    def add(self, number: int) -> None:
        self.num_fre_tracker[self.frequency_tracker[number]] -=1
        if self.num_fre_tracker[self.frequency_tracker[number]] <= 0:
            self.num_fre_tracker.pop(self.frequency_tracker[number])
        self.frequency_tracker[number] += 1
        self.num_fre_tracker[self.frequency_tracker[number]] +=1

    def deleteOne(self, number: int) -> None:
        self.num_fre_tracker[self.frequency_tracker[number]] -=1
        if self.num_fre_tracker[self.frequency_tracker[number]] <= 0:
            self.num_fre_tracker.pop(self.frequency_tracker[number])
        self.frequency_tracker[number] -= 1
        if self.frequency_tracker[number] <= 0:
            self.frequency_tracker.pop(number)

        self.num_fre_tracker[self.frequency_tracker[number]] +=1


    def hasFrequency(self, frequency: int) -> bool:
        return self.num_fre_tracker[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)