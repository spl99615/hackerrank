

def main(a, item):
    low = 0
    high = len(a) - 1
    mid = (low + high) / 2

    guess = a[mid]

    while(guess != item):
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        mid = (low + high) / 2
        guess = a[mid]
    return mid


if __name__ == '__main__':
    print(main([1, 4, 8, 9, 25, 100, 340, 567, 1000], 340))
