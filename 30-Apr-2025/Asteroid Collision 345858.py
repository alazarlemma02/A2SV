# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        st = []

        for asteroid in asteroids:
            while st and st[-1] > 0 and asteroid < 0:
                if abs(st[-1]) > abs(asteroid):
                    asteroid = 0
                elif abs(st[-1]) < abs(asteroid):
                    st.pop()
                else:
                    asteroid = 0
                    st.pop()
            if asteroid:
                st.append(asteroid)
                      
        return st