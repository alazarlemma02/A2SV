# Problem: D - Electric Mayhem - https://codeforces.com/gym/605795/problem/D

def solve(chars):
    st = []
    st.append(chars[0])

    if (len(chars)%2):
        return "No"
    
    for c in range(1, len(chars)):
        if not st or chars[c] != st[-1]:
            st.append(chars[c])
        else:
            st.pop()

    if not st:
        return "Yes"
    return "No"

chars = str(input())
print(solve(chars))