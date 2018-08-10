import re

import requests
from bs4 import BeautifulSoup
from pandas import pandas as pd

search_url = 'https://www.tianyancha.com/search?key=={0}'
file_tem = '../enterprise_info_{0}.csv'


def hot_tyc(keyword):
    url = search_url.format(keyword)
    projects = get_enterprise(url)
    print("搜索结果总数为: {0}".format(len(projects)))
    hotdf = pd.DataFrame(persistent_structure(projects))
    file_path = file_tem.format(re.sub("\s+", "_", keyword))
    hotdf.to_csv(file_path, index=False)
    return file_path


def get_enterprise(url):
    html = requests.get(url).content.decode('utf-8')
    # Python的内置标准库, 执行速度适中, 文档容错能力强
    soup = BeautifulSoup(html, 'html.parser')
    pro_list = []
    search_result = soup.find_all("div", class_="search_result_single")
    for index, li in enumerate(search_result):
        pro_info = render_pro_info(li)
        pro_list.append(pro_info)

    return pro_list


def render_pro_info(li_tag):
    data = {}
    right = li_tag.find("div", class_="search_right_item")
    data["name"] = right.find("div").find("span").strip()
    return data


def persistent_structure(proInfos):
    name = []
    representative = []
    capital = []
    date = []
    address = []
    for item in proInfos:
        name.append(item["name"])
        representative.append(item["representative"])
        capital.append(item["capital"])
        date.append(item["date"])
        address.append(item["address"])

    return {"企业名称": name, "法定代表人": representative, "注册资本": capital, "注册时间": date, "地址信息": address}


if __name__ == '__main__':
    keyword = input('请输入想要查找的关键词:')
    file = hot_tyc(keyword)
    print("请到下面目录地址获取查看得到的项目信息:{0}".format(file))

