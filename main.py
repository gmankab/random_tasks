#!/bin/python

import pytest

list1 = [4, 8, 1, 15]
list2 = [4, 8, 3, 15, 16, 23, 421]
list3 = [4, 8, 1, 16]

possible_replacement = {
    1: 3,
    2: 4,
    3: 1,
    4: 2,
}


def ordered_comparison(
    list_1,
    list_2,
):
    index = -1
    while True:
        index += 1
        if (
            index >= len(list_1)
        ) and (
            index >= len(list_2)
        ):
            return []

        if index >= len(list_1):
            return list_2[index:]

        if index >= len(list_2):
            return list_1[index:]

        num_1 = list_1[index]
        num_2 = list_2[index]

        if num_1 == num_2:
            continue

        if (
            num_1 in possible_replacement
        ) and (
            num_2 == possible_replacement[num_1]
        ):
            continue

        raise Exception(
            'elements are not equal'
        )


assert ordered_comparison(list1, list2) == [16, 23, 421]


with pytest.raises(Exception):
    print(ordered_comparison(list1, list3))
