#!/bin/env/ python3


def sockMerchant(n, ar):
    color_set = set(ar)
    color_map = {}
    for color in ar:
        if color in color_set:
            color_map[color] = color_map.get(color, 0) + 1
    # print(color_map)
    no_pairs = sum([color_map[key] // 2 for key in color_map if color_map[key] >= 2])
    # print(no_pairs)
    return no_pairs


if __name__ == "__main__":
    no_pairs = sockMerchant(7, [1, 2, 3])
    print(no_pairs)
