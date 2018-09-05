#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Hinsteny 2018 ActiveState Software Inc.

import os


def mk_file_folder(file_path):
    """make dir recursive for given file_path"""
    folder_path = os.path.dirname(file_path)
    is_exists = os.path.exists(folder_path)
    if not is_exists:
        os.makedirs(folder_path)


def write_content_to_file(file_path, content):
    """write content to file by file_path"""
    mk_file_folder(file_path)
    with open(file_path, 'w') as f:
        f.write(content)
    print("write file success!")


def get_file_outer(file_path):
    """open file return outer"""
    mk_file_folder(file_path)
    outer = open(file_path, 'w')
    return outer


def read_file_by_line_to_list(file_path):
    """"read file content bu line and collect to list"""
    f = open(file_path, "r")
    lines = f.readlines()
    f.close()
    return lines


if __name__ == '__main__':
    filePath = "E:/data/python/test.txt"
    content = "Hello World!"
    write_content_to_file(filePath, content)
