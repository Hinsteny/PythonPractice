#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Hinsteny 2018 ActiveState Software Inc.

""""题目
给定一个字符串, 请你找出其中不含有重复字符串的 最长子串 的长度
示例 1：
    输入: “abcabcbb”
    输出: 3
    解释: 因为无重复字符的最长子串是"abc", 所以其长度为3.

示例 2：
    输入: "bbbbbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是"b", 所以其长度为1.

示例 3：
    输入: "abcdb12"
    输出: 5
    解释: 因为无重复字符的最长子串是"cdb12", 所以其长度为5.
"""

""""答案
对给定字符str(length=n)串进行迭代处理, 使用滑动窗口(子串)记录不重复的子串内容, 每次遇到重复子符时, 需要将滑动窗口的开始位置移动到重复字符后一位, 
每次处理完一个字符时, 都计算当前最大子串长度, 当迭代完整个母字符串时, max所记录值即为最大不重复字符子串长度;
"""


def getMaxSubstrLength(str):
    max = 0
    substr = ""
    for i in range(0, len(str)):
        index = substr.find(str[i])
        if index > -1:
            substr = substr[index + 1:]
        substr += str[i]
        max = (max if (max > len(substr)) else len(substr))
    return max


if __name__ == '__main__':
    while True:
        str = input('请输入给定一个字符串:')
        print(getMaxSubstrLength(str))
