import urllib.request
import urllib.parse

# # 获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com/")
# # decode()对获得的网页源码进行utf-8解码
# print(response.read().decode('utf-8'))

# # 获取一个post请求
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(response.read().decode("utf-8"))

# # 超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out")

# 响应头
# response = urllib.request.urlopen("http://baidu.com", timeout=1)
# print(response.getheader("Server"))


# # 使用request对象
# url = "http://httpbin.org/post"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/87.0.4280.88 Safari/537.36 "
# }
# data = bytes(urllib.parse.urlencode({'name': 'eric'}), encoding="utf-8")
# req = urllib.request.Request(url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


# # 豆瓣
# url = "https://www.douban.com"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/87.0.4280.88 Safari/537.36 "
# }
# req = urllib.request.Request(url, headers=headers)
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))
