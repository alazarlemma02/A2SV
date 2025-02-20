# Problem: E - Zombie Invasion! - https://codeforces.com/gym/588094/problem/E

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))

    zombies = sorted(zip(x,a), key= lambda z: abs(z[0]))
    is_dead = True
    total_needed_bullets = 0

    for z in range(n):
        xi, ai = zombies[z]

        total_needed_bullets += ai

        can_shoot = abs(xi)* k

        if total_needed_bullets > can_shoot:
            is_dead = False
            break
    print("YES" if is_dead else "NO")