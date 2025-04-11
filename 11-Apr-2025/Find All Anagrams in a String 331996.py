# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)

        p_cnt = Counter(p)
        s_cnt = defaultdict(int)
        i, res = 0, []

        for j in range(n):
            s_cnt[s[j]] +=1

            if j - i + 1 == m:
                if s_cnt == p_cnt:
                    res.append(i)
                    
                s_cnt[s[i]] -=1
                if s_cnt[s[i]] == 0:
                    del s_cnt[s[i]]
                i +=1
        return res