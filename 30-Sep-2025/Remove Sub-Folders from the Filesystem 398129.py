# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = [folder[0]]
      
        for curr in folder[1:]:
            last_f = result[-1]
            last_len = len(last_f)
            curr_len = len(curr)

            not_subfld = (last_len >= curr_len or 
                                 not (last_f == curr[:last_len] and 
                                      curr[last_len] == '/'))
          
            if not_subfld:
                result.append(curr)
      
        return result