
# x guaranteed to be greater or equal to y
def subtract(n, base):
    l = len(n)

    nasc = sorted(n)
    ndesc = nasc[::-1]

    for i in range(l - 1, -1, -1):
        if nasc[i] < ndesc[i]:
            nasc[i] += base
            nasc[i - 1] -= 1

        nasc[i] -= ndesc[i]

    return nasc


def key(s):
    k = 0
    for i in range(len(s)):
        k += int(s[i]) * (10 ** i)

    return k


def solution(n, b):
    seen = {}
    x = [int(d) for d in list(n)]
    i = 0

    while True:
        xkey = key(x)
        if xkey in seen:
            return i - seen[xkey]

        seen[xkey] = i
        x = subtract(x, b)
        i += 1


if __name__ == '__main__':
    print(solution('210022', 3))
    print(solution('1211', 10))
