def main():
    base_url = "https://movie.douban.com/top250"
    # 爬取网页
    datalist = get_data(base_url)
    save_path = ".\\doubanMovieTop250.xls"
    # 保存数据
    save_data(save_path)


def get_data(baseurl):
    data_list = []
    return data_list


def save_data(savepath):
    print("save...")
