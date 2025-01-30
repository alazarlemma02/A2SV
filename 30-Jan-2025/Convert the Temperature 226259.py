# Problem: Convert the Temperature - https://leetcode.com/problems/convert-the-temperature/

class Solution(object):
    def convertTemperature(self, celsius):
        kelvin = celsius + 273.15
        fah = celsius * 1.80 + 32.00
        return [kelvin, fah]
        