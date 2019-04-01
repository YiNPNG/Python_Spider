import re

# regex = re.compile(r'\w+')

# regex = re.compile(r'\w+',flags=re.A)

# 匹配时忽略大小写
# regex = re.compile(r'[a-z]+',flags=re.I)

# ．可以匹配换行
# regex = re.compile(r'.+',flags=re.S)

# ^$ 匹配每一行开头结尾
# regex = re.compile(r'^达内',flags=re.M)

# 为正则添加注释
# pattern = r'''[A-Z]\w+ # 第一个单词
# \s+\w+\s+       # 空格和第二个单词
# \S+         # 匹配汉字
# '''
# regex = re.compile(pattern,flags=re.X)

# s = """Welcome to
# 达内
# """

# l = regex.findall(s)
# print(l)

s = re.sub(r'\.','-','1024.45.12')
print(s)
