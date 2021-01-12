# 正则表达式：字符串模式，判断字符串是否符合一定的标准
import re

# 创建模式对象
# AA是正则表达式
pat = re.compile("AA")

# search方法进行比对查找,匹配首个找到的结果,返回一个match对象
# 用模式对象匹配
# m = pat.search("ABCAA")
# m = pat.search("AABCAADDCCAA")
# print(m)
# print(type(m))

# 直接用字符串匹配
# m = re.search("asd", "Aasd")
# print(m)

# findall()匹配所有结果,返回一个包含所有结果的列表
# print(re.findall("a", "ASFDSFJNFaFSDAAa"))
# print(re.findall("[A-Z]", "ASFDSFJNFaFSDAAa"))

# print(re.findall("[A-Z]+", "ASFDSFJNFaFSDAAa"))

# 找到a,用A替换
print(re.sub("a", "A", "asdfsafdsa"))

# 建议在正则表达式中，被比较的字符串起前面加上r，防止转义字符生效
a = r"v\a\l\r\v[vs"
print(a)