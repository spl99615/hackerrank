def repeatedString(s, n):
    if s == 'a':
        return n
    if n % len(s) == 0:
        lenrep = n // len(s)
    else:
        lenrep = n // len(s) + 1
    rep_str = s * lenrep
    substring = rep_str[0:n + 1]
    return sum([1 for s in substring if s == 'a'])


if __name__ == '__main__':
    s = 'abaxxxxx'
    n = 100000000
    result = repeatedString(s, n)
    print(result)
