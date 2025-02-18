# Problem: C - Barking Password - https://codeforces.com/gym/588094/problem/C

password = input()
n = int(input())
words = []

for s in range(n):
    word = input()
    words.append(word)

if password in words:
    print("YES")
    exit()

first_char = False
for word in words:
    if word[1] == password[0]:
        first_char = True
        break

second_char = False
for word in words:
    if word[0] == password[1]:
        second_char = True
        break

if first_char and second_char:
    print("YES")
else:
    print("NO")
