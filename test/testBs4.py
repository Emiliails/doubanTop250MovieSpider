import testRe

from bs4 import BeautifulSoup

# Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:
# Tag , NavigableString , BeautifulSoup , Comment .

file = open("./baidu.html", "rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")

# -------------------------4种对象概述
# tag

# 打印拿到的第一个标签及其内容
# print(bs.title)
# print(bs.a)
# print(bs.head)
# print(type(bs.title))


# 打印标签内的内容(NavigableString)
# print(bs.title.string)
# print(type(bs.title.string))

# 以字典方式获取标签内所有属性，以字典方式呈现
# print(bs.a.attrs)

# beautifulSoup，即整个文档
# print(type(bs))

# comment 特殊的NavigableString，输出的内容不包含注释符
# print(bs.a.string)
# print(type(bs.a.string))

# --------------------------------------文档遍历
# contents获取tag的所有子节点。返回一个list
# print(bs.head.contents)
# print(bs.head.contents[0])

# --------------------------------------文档搜索
# ------1find_all()
# 字符串匹配，会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")
# print(t_list)

# 正则表达式搜索
# t_list = bs.find_all(re.compile("a"))
# print(t_list)


# 函数
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
#
# t_list = bs.find_all(name_is_exists)
#
# for item in t_list:
#     print(item)
#
# # print(t_list)

# ------2.kwargs 参数
# t_list = bs.find_all(id="head")
# for item in t_list:
#     print(item)

# t_list = bs.find_all(class_=True)
# for item in t_list:
#     print(item)

# t_list = bs.find_all(href="http://news.baidu.com")
# for item in t_list:
#     print(item)

# -------3.text 参数
# t_list = bs.find_all(text="hao123")
# t_list = bs.find_all(text=["hao123", "地图", "贴吧"])
# for item in t_list:
#     print(item)
# 使用正则表达式查找带数字的标签里的字符串
# t_list = bs.find_all(text=re.compile("\d"))
# for item in t_list:
#     print(item)
# --------4. limit参数
# t_list = bs.find_all("a", limit=2)
# for item in t_list:
#     print(item)

# ----------------------------css选择器
# 通过标签查找
# t_list = bs.select('title')
# for item in t_list:
#     print(item)
# 通过类名查找
# t_list = bs.select(".mnav")
# for item in t_list:
#     print(item)
# 通过id查找
# t_list = bs.select("#u1")
# for item in t_list:
#     print(item)
# 通过属性查找
# t_list = bs.select("a[class='bri']")
# for item in t_list:
#     print(item)
# 通过子标签查找
# t_list = bs.select("head > title")
# for item in t_list:
#     print(item)
# 通过兄弟节点查找
# t_list = bs.select(".mnav ~ .bri")
#
# print(t_list[0].get_text())
