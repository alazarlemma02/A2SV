# Problem: Convert a String to an Integer using Recursion - https://www.geeksforgeeks.org/convert-a-string-to-an-integer-using-recursion/

def convert(s, idx):
  if idx == len(s)-1:
    return int(s[idx])
    
  curr = int(s[idx])
  
  return curr * (10 ** (len(s)-idx-1)) + (convert(s, idx+1))


def stringToInt(s):
  return convert(s, 0)