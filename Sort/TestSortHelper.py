# -*- coding: utf-8 -*-
# @Time    : 2018/8/5 14:47
# @Author  : GaoLei
# @File    : TestSortHelper.py
# @Software: PyCharm
import random
import string


def generate_random_array(n, range_l, range_r):
    arr = []
    assert range_l <= range_r
    for i in range(n):
        arr.append(random.randint(range_l, range_r))
    return arr


def generate_random_string_array(n):
    arr = []
    for i in range(n):
        arr.append(random.sample(string.ascii_letters, 1)[0])
    return arr


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __le__(self, other):
        if self.score <= other.score:
            return True


def generate_random_class_array(n):
    name_array = []
    arr = []
    for i in range(n):
        name_array.append('student%s' % i)
    for i in range(n):
        t = Student(name_array[i], random.randint(10, 15))
        arr.append(t)
    return arr
