# Problem: Decimal to binary number using recursion - https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/

# Decimal to binary conversion
# using recursion
def dec_to_bin(d):
  if d // 2 == 0:
    return d
  
  res = dec_to_bin(d//2)
  return d % 2 + res * 10
    

# Driver code 
d = 23
print(dec_to_bin(d))