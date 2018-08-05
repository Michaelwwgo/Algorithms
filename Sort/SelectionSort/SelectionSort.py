# -*- coding: utf-8 -*-
# @Time    : 2018/8/5 14:08
# @Author  : GaoLei
# @File    : SelectionSort.py
# @Software: PyCharm
import TestSortHelper


def selection_sort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[j] <= array[i]:
                array[i], array[j] = array[j], array[i]
    return array


if __name__ == '__main__':

    sort_result = selection_sort(TestSortHelper.generate_random_class_array(20))
    for i in sort_result:
        print('%s:%d' % (i.name, i.score))
