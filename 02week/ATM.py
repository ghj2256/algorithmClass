def func(n):
    answer = 0
    p = list(map(int, input().split()))
    while n != len(p):
        print("Input again!")
        p = list(map(int, input().split()))
    p.sort()
    for i in range(len(p)+1):
        answer += sum(p[:i])
    return answer


if __name__ == "__main__":
    a = int(input())
    print(func(a))
