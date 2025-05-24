# Problem: Recursively remove all adjacent duplicates - https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

#User function Template for python3

class Solution:
    def removeUtil (self, S):
		#code here
		
	    def remove(s):
    		res = ''
    		i, n = 0, len(s)
    		
    		while i < n:
    		    if i < n-1 and s[i] == s[i+1]:
    		        while i < n-1 and s[i] == s[i+1]:
    		            i +=1
		            i +=1
    		    else:
    		        res += s[i]
    	            i +=1
    	        
    	    return res
    	    
	    prev = ""
	    
	    while S != prev:
	        prev = S
	        S = remove(S)
	        
        return S