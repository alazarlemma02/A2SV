# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

num = int(input())
cnt = 0

for i in range(2, num + 1):
    prime_divisors = 0
    for j in range(2, i + 1):
        if i % j == 0:
            is_prime = True
            for k in range(2, int(j ** 0.5) + 1):
                if j % k == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_divisors += 1
    if prime_divisors == 2:
        cnt += 1
print(cnt)