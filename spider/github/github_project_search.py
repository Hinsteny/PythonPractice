import re

import requests
from bs4 import BeautifulSoup
from bs4 import element
from pandas import pandas as pd

main_url = 'https://github.com{0}'
search_url = 'https://github.com/search?q={0}&ref=simplesearch&type=Repositories&utf8=%E2%9C%93/'
file_tem = './github_hot_{0}.csv'


def hot_github(keyword, total):
    url = search_url.format(keyword)
    projects = get_projects(url, [], total)
    print("搜索结果总数为: {0}".format(len(projects)))
    hotdf = pd.DataFrame(persistent_structure(projects))
    file_path = file_tem.format(re.sub("\s+", "_", keyword))
    hotdf.to_csv(file_path)
    return file_path


def get_projects(url, pro_list, total):
    html = requests.get(url).content.decode('utf-8')
    # Python的内置标准库, 执行速度适中, 文档容错能力强
    soup = BeautifulSoup(html, 'html.parser')
    # soup = BeautifulSoup(html, 'lxml')
    searchTotal = getSearchTotal(soup)
    if searchTotal == 0:
        return pro_list[0:total]
    if searchTotal != 0:
        total = (total if total > searchTotal else total)
        ul = soup.find("ul", class_="repo-list")
        if ul:
            li_list = ul.find_all("div", class_="repo-list-item")
            for index, li in enumerate(li_list):
                pro_info = render_pro_info(li)
                pro_list.append(pro_info)

        if len(pro_list) < total:
            page = soup.find("div", class_="pagination")
            if page:
                next_page = page.find("a", class_="next_page")
                return get_projects(main_url.format(next_page["href"]), pro_list, total)
    return pro_list[0:total]


def getSearchTotal(soup):
    codesearch = soup.find("div", class_="codesearch-results")
    count = -1
    if codesearch.find("div", class_="blankslate"):
        count = 0
    if count == -1:
        h3 = codesearch.find("h3")
        if len(h3.contents) > 0:
            count_str = h3.contents[0]
            if count_str.strip() != '':
                count = int(re.sub("\D", "", count_str))
    return count


def render_pro_info(li_tag):
    data = {}
    header = li_tag.find("h3").find("a")
    data["href"] = main_url.format(header["href"])
    h_cont = get_tag_contents(header, "")
    num_dis = h_cont.find('/')
    data["auther"] = h_cont[0: num_dis]
    data["title"] = h_cont[num_dis+1:]
    description = li_tag.find("p")
    if description:
        data["description"] = get_tag_contents(description, "").strip()
    return data


def get_tag_contents(parent, str):
    for item in parent.contents:
        if type(item) is element.NavigableString:
            str += item
        else:
            return get_tag_contents(item, str)
    return str


def persistent_structure(proInfos):
    titles = []
    descriptions = []
    hrefs = []
    authers = []
    for item in proInfos:
        titles.append(item["title"])
        descriptions.append(item["description"])
        hrefs.append(item["href"])
        authers.append(item["auther"])

    return {"地址": hrefs, "作者": authers, "项目简介": descriptions, "项目名称": titles}


if __name__ == '__main__':
    keyword = input('请输入想要查找的关键词:')
    total = int(input('请输入想要获取的总记录条数(输入值应该是大于0的整数):'))
    file = hot_github(keyword, total)
    print("请到下面目录地址获取查看得到的项目信息:{0}".format(file))

