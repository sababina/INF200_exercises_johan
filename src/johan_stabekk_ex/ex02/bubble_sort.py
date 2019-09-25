# -*- coding: utf-8 -*-


def bubble_sort(data):
    data_sorted = list(data)

    for i in range(0, len(data_sorted) - 1):
        for j in range(0, len(data_sorted) - 1 - i):
            if data_sorted[j] > data_sorted[j + 1]:
                data_sorted[j], data_sorted[j+1] = data_sorted[j+1], data_sorted[j]

    return data_sorted


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
