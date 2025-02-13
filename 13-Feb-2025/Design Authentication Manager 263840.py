# Problem: Design Authentication Manager - https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.auth_map = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.auth_map[tokenId] = currentTime + self.timeToLive


    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.auth_map:
            if currentTime < self.auth_map[tokenId]:
                self.auth_map[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token in self.auth_map:
            if self.auth_map[token] > currentTime:
                count +=1
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)