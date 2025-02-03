# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

for i in range(int(input())):
    word = input()
    if len(word) <= 10:
        print(word)
    else:
        first_letter, last_letter = word[0], word[-1]
        between_count = len(word)-2
        result = f"{first_letter}{between_count}{last_letter}"
        print(result)
