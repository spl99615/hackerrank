def reduction_cost(arr):
    # n = len(arr)
    # cost_arr = []

    if len(arr) <= 2:
        return sum(arr)
    # else:
    #     cost, a = two_elements(arr)
    #     #print(cost, a)
    #     cost_arr.append(cost)
    #     while a is not None:
    #         cost, a = two_elements(a)
    #         cost_arr.append(cost)
    # return sum(cost_arr)
    summ = 0
    while len(arr) > 2:
        arr = sorted(arr)
        summ += arr[0] + arr[1]
        arr = [(arr[0] + arr[1])] + arr[2:]
    summ += sum(arr)
    return summ


def two_elements(arr):
    tmp_arr = list(arr)
    if len(tmp_arr) <= 2:
        return tuple([sum(tmp_arr), None])
    else:
        tot = sum(tmp_arr[:2])
        del tmp_arr[:2]
        tmp_arr.append(tot)
        #print("tot::{} tmp_arr{}".format(tot, tmp_arr))
        return tuple([tot, tmp_arr])


if __name__ == '__main__':
    c = reduction_cost([1, 2, 3, 4, 5, 6])
    print(c)
