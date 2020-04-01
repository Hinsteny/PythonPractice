#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) Hinsteny 2020 ActiveState Software Inc.

import sys
sys.path.append("..")
from common.FileUtils import *

def read_file_by_line_to_list(file_path):
    """"read file content bu line and collect to list"""
    f = open(file_path, "r")
    lines = f.readlines()
    f.close()
    return lines


def write_content_to_file(file_path, content):
    """write content to file by file_path"""
    with open(file_path, 'w') as f:
        for item in content:
            f.write(item + "\n")
    print("write file success!")


def renderData(dataList):
    newData = []
    for item in dataList:
        splits = item.split()
        newItem = "UPDATE health_product_spu2sku SET eip_sku_code = \"" + splits[0] + "\" WHERE spu_code = \"" + splits[1] + "\" AND sku_code = \""  + splits[2] + "\" AND eip_sku_code = \""  + splits[3] + "\";"
        newData.append(newItem)
    return newData


if __name__ == '__main__':
    filePath = "/Users/hinsteny/Documents/文档/线上SQL/无规格商品关联EipSkuCode修改/刷表原始数据"
    data = FileUtils.read_file_by_line_to_list(filePath + ".txt")
    newData = renderData(data)
    write_content_to_file(filePath + ".sql", newData)
