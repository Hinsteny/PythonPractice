import requests
import re
from bs4 import BeautifulSoup
from bs4 import element
from pandas import pandas as pd

main_url = 'https://github.com{0}'
search_url = 'https://github.com/search?q={0}&ref=simplesearch&type=Repositories&utf8=%E2%9C%93/'
file_tem = '../../tmp/github_hot_{0}.csv'


def hot_github(keyword, total):
    url = search_url.format(keyword)
    projects = get_projects(url, [], total)
    print(len(projects))
    hotDF = pd.DataFrame(persistent_structure(projects))
    file_path = file_tem.format(re.sub("\s+", "_", keyword))
    hotDF.to_csv(file_path, index=False)
    return file_path


def get_projects(url, pro_list, total):
    print(len(pro_list))
    html = requests.get(url).content.decode('utf-8')
    # soup = BeautifulSoup(html_doc, 'html.parser') # Python的内置标准库, 执行速度适中, 文档容错能力强
    soup = BeautifulSoup(html, 'lxml')
    ul = soup.find("ul", class_="repo-list js-repo-list")
    if ul:
        li_list = ul.find_all("li")
        for index, li in enumerate(li_list):
            pro_info = render_pro_info(li)
            pro_list.append(pro_info)

    if len(pro_list) < total:
        page = soup.find("div", class_="pagination")
        if page:
            next_page = page.find("a", class_="next_page")
            return get_projects(main_url.format(next_page["href"]), pro_list, total)
    return pro_list[0:total]


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
        data["description"] = get_tag_contents(description, "")
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

