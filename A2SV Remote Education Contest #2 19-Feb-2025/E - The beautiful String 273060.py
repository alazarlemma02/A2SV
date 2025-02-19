# Problem: E - The beautiful String - https://codeforces.com/gym/586622/problem/E

t = int(input())

for _ in range(t):
    s = list(input())
    q = int(input())
    idx_set = set()

    for b in range(len(s)):
      if s[b:b+4] == ['1', '1', '0', '0']:
         idx_set.add(b)
    for _ in range(q):
      idx, val = map(int, input().split())
      idx -= 1
      if s[idx] == str(val):
         print("YES" if idx_set else "NO")
         continue
      s[idx] = str(val)
      start = max(idx-3, 0)
      end = min(len(s)-3, idx+1)
      for i in range(start, end):
          if s[i:i+4] == ['1', '1', '0', '0']:
            idx_set.add(i)
          else:
             idx_set.discard(i)
      print("YES" if idx_set else "NO")