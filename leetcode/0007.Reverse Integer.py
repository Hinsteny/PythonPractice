#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Hinsteny 2019 ActiveState Software Inc.

"""题目--整数反转
给出一个32位的有符号整数, 你需要将这个整数中每位上的数字进行反转
示例 1：
    输入: 123
    输出: 321

示例 2：
    输入: -123
    输出: -321

示例 3：
    输入: 120
    输出: 21
"""

"""答案
将整数转化为字符串, 取出符号位(+,-), 然后对剩下的数字字符序列进行一个倒置, 最后再将倒置的字符串解析为一个新的整数
"""


def splitStr(number):
    arrays = []
    for i in range(0, len(number)):
        arrays.append(number[i])
    return arrays


def getRevertNumber(number):
    arr = splitStr(number)
    length = len(arr) - 1
    for i in range(0, length // 2):
        x = arr[i]
        arr[i] = arr[length - i]
        arr[length - i] = x
    while arr[0] == "0":
        arr = arr[1:]
    return ''.join(arr)


if __name__ == '__main__':
    while True:
        number = input('请输入给定一个整数:')
        symbol = ""
        if number.startswith("-"):
            symbol = symbol.join("-")
            number = number[1:]
        if number.isdigit():
            print(symbol + getRevertNumber(number))
        else:
            print("输入内容非整数")
