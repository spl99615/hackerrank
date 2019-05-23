

def kthLargest(arr, k):
    arr = sorted(arr, reverse=True)
    print(arr)
    return arr[k - 1]


def kthSmallest(arr, k):
    arr = sorted(arr)
    print(arr)
    return arr[k - 1]


if __name__ == '__main__':
    print(kthLargest([25, 5, 8, 13, 2, 7], 5))
    print(kthSmallest([12, 3, 5, 7, 19], 2))
