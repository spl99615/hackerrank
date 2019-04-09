def getMoneySpent(keyboards, drives, b):
    budget_arr = []
    for keyboard in keyboards:
        if keyboards == b:
            continue
        for drive in drives:
            if drive == b:
                continue
            if (keyboard + drive) <= b:
                budget_arr.append(keyboard + drive)
    if not budget_arr:
        return -1
    else:
        return max(budget_arr)


if __name__ == '__main__':
    maxbudget = getMoneySpent([4], [5], 5)
    print(maxbudget)
