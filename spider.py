import re
import sqlite3
import urllib.request
import urllib.error

from bs4 import BeautifulSoup


def main():
    # 爬取网页
    base_url = "https://movie.douban.com/top250?start="
    datalist = get_data(base_url)

    # 保存数据至xls
    # save_path = ".\\doubanMovieTop250.xls"
    # save_data(save_path)

    # 保存数据至sqlite
    db_path = 'movie.db'
    saveData2DB(datalist, db_path)


# 用于获取影片详情链接的正则表达式对象
findLink = re.compile(r'<a href="(.*?)">')

# 用于获取影片图片的链接的正则表达式对象
# re.S使换行符包含在内
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)

# 用于获取片名的正则表达式对象
findTitle = re.compile(r'<span class="title">(.*)</span>')

# 用于获取评分的正则表达式对象
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')

# 用于获取评价人数的正则表达式对象
findJudge = re.compile(r'<span>(\d*)人评价</span>')

# 用于获取概况的正则表达式对象
findInq = re.compile(r'<span class="inq">(.*)</span>')

# 用于获取影片相关内容的正则表达式对象
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def get_data(baseurl):
    data_list = []

    # 调用ask_url10次以获取250条电影信息
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = ask_url(url)
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        # 查找符合要求的字符串形成列表:div元素，class属性为item
        for item in soup.find_all('div', class_="item"):
            # 保存一部电影的所有信息
            data = []
            item = str(item)

            # 获取影片详情链接
            link = re.findall(findLink, item)[0]
            data.append(link)

            # 获取封面图片
            img_src = re.findall(findImgSrc, item)[0]
            data.append(img_src)

            # 获取不同语言的影片名称
            titles = re.findall(findTitle, item)

            # 仅有中外两种名称时
            if len(titles) == 2:
                # 中文名称
                chinese_title = titles[0]
                data.append(chinese_title)

                # 外文名称
                # replace用于去掉无关的符号
                foreign_title = titles[1].replace("/", "")
                data.append(foreign_title)
            else:
                # 中文名称
                data.append(titles[0])
                # 外文名称留空
                data.append('')

            # 添加评分
            rating = re.findall(findRating, item)[0]
            data.append(rating)

            # 添加评价人数
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)

            # 添加概述
            inq = re.findall(findInq, item)

            # 存在影片无概述的情况
            # 去除影片概述中的句号
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
            else:
                inq = " "

            data.append(inq)

            bd = re.findall(findBd, item)[0]
            # 去掉<br/>
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)
            # 替换 /
            bd = re.sub('/', ' ', bd)
            # 去掉空格
            data.append(bd.strip())

            data_list.append(data)

    print(data_list)

    return data_list


# 得到指定一个URL的网页内容
def ask_url(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    request = urllib.request.Request(url, headers=head)

    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存数据
def save_data(save_path):
    print("save...")


def saveData2DB(datalist, db_path):
    init_db(db_path)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # datalist中有250个data
    for data in datalist:

        # 拼接sql语句
        # 每个data中有8个item
        for index in range(len(data)):
            # 给除了打分和评论人数以外的每个item加上双引号便于嵌入sql
            if index == 4 or index == 5:
                continue
            data[index] = '"' + data[index] + '"'

        # ",".join(data)表示将data列表中的每个item用逗号分隔
        # %s是占位符，用",".join(data)填充
        # print(data)
        sql = '''
            insert into movie250(
            info_link,pic_link,cname,ename,score,rated,introduction,info
        )
            values (%s)''' % ",".join(data)

        print(sql)
        cur.execute(sql)
        print("1")
        conn.commit()
    cur.close()
    conn.close()


def init_db(db_path):
    sql = '''
        create table movie250
        (
            id        integer primary key autoincrement,
            info_link text,
            pic_link  text,
            cname     varchar,
            ename     varchar,
            score     numeric,
            rated     numeric,
            introduction text,
            info text
        )
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
