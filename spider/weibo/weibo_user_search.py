#!/usr/bin/env python
# -*- coding: utf-8 -*-
# search weibo user name
# Copyright (c) Hinsteny 2018 ActiveState Software Inc.

import re
import requests
from bs4 import BeautifulSoup
from bs4 import element
from urllib.parse import urlencode
from pandas import pandas as pd

main_url = ''
search_url = 'https://s.weibo.com/user?q={0}&Refer=index&page={1}'
file_tem = './web_user_{0}.csv'


def hot_weibo(keyword, total, page):
    users = []
    while len(users) < total:
        url = search_url.format(keyword, page)
        result = get_users(url, users, total, page)
        if not result:
            break
        page += 1
    print("搜索结果总数为: {0}".format(len(users)))
    # hotdf = pd.DataFrame(persistent_structure(projects))
    # file_path = file_tem.format(re.sub("\s+", "_", keyword))
    # hotdf.to_csv(file_path)
    return users


def get_users(url, user_list, total, page):
    html = requests.get(url).content.decode('utf-8')
    # Python的内置标准库, 执行速度适中, 文档容错能力强
    soup = BeautifulSoup(html, 'html.parser')
    # soup = BeautifulSoup(html, 'lxml')
    parent = soup.find("div", class_="card-wrap")
    if parent:
        childs = parent.find_all("div", class_="card-user-b")
        if len(childs) > 0:
            for index, item in enumerate(childs):
                user_info = render_user_info(item)
                user_list.append(user_info)
            return True
        else:
            return False


def render_user_info(dev_tag):
    data = {}
    info = dev_tag.find("div", class_="info")
    name_a = info.find("div").find("a", class_="name")
    name = name_a.text
    data["name"] = name
    data["description"] = get_user_description(info.find_all("p"))
    return data


def get_user_description(container):
    description = "无简介"
    if len(container) > 0:
        for item in container:
            text = item.text
            if len(text) > 0 and text.find("简介：") > -1:
                description = text[4:len(text)]
                break
    return description


if __name__ == '__main__':
    keyword = input('请输入想要查找的用户昵称关键词:')
    # total = int(input('请输入想要获取的总记录条数(输入值应该是大于0的整数):'))
    total = 100
    users = hot_weibo(keyword, total, 1)
    print("搜索到的用户信息如下")
    for index, item in enumerate(users):
        print("[{0}]  昵称: {1}, 简介: {2}".format(index + 1, item["name"], item["description"]))

