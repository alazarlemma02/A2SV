# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    result = []
    for _ in range(N):
        command = input().split()
        com = command[0]
        if com == "insert":
            result.insert(int(command[1]), int(command[2]))
        elif com == "remove":
            result.remove(int(command[1]))
        elif com == "append":
            result.append(int(command[1]))
        elif com == "reverse":
            result.reverse()
        elif com == "pop":
            result.pop()
        elif com == "sort":
            result.sort()
        else:
            print(result)