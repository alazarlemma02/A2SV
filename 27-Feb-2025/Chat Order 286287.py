# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

from collections import OrderedDict

def chatOrder(n):
    chat_map = OrderedDict()

    for _ in range(n):
        msgr = input()
        if msgr in chat_map:
            del chat_map[msgr]
        chat_map[msgr] = True

    print("\n".join(reversed(chat_map.keys())))

n = int(input())
chatOrder(n)