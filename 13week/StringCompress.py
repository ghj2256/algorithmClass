def solution(s):
    result = len(s)
    for i in range(1, int(len(s)/2)+1):
        length = len(s)
        for j in range(len(s)):
            for z in range(i, len(s), i):
                count = 0
                if j+z >= len(s):
                    break
                if s[j:i] == s[j+z:i]:
                    count += 1
                else:
                    length -= i*count
                    if count:
                        length += len(str(count + 1))
                    j += z-1
                    break
                if j+z+i >= len(s):
                    length -= i*count
                    length += len(str(count + 1))
                    j += z
        if length < result:
            result = length
    return result


if __name__ == "__main__":
    string = "abcabcdede"
    answer = solution(string)
    print(answer)
