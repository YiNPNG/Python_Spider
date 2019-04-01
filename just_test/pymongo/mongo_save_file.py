from pymongo import MongoClient
import bson.binary

conn = MongoClient('localhost',27017)
db = conn.image
myset = db.mm

# 存储图片
# f = open('timg.jfif','rb')
# data = f.read()

# # 转换bson 格式
# content = bson.binary.Binary(data)

# myset.insert_one({'filename':'timg.jfif','data':content})

# 文件提取
img = myset.find_one({'filename':'timg.jfif'})

# 将data写入新文件
with open('mm.jfif','wb') as f:
    f.write(img['data'])

conn.close()