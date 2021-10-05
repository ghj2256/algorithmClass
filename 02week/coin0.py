def func(n, k):
    answer = 0
    coin = []
    for i in range(n):
        coin.append(int(input()))
    coin.reverse()

    for i in coin:
        answer += k // i
        k %= i
    return answer


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(func(a, b))
