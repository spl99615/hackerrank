def countingValleys(n, s):
    no_valleys = 0
    base = 0
    for step in s:
        if step == 'U':
            base += 1
            if base == 0:
                no_valleys += 1
        else:
            base -= 1
    return no_valleys


if __name__ == '__main__':
    print(countingValleys(8, 'DDDUDUU'))
