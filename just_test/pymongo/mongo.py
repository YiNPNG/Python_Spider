from pymongo import MongoClient
import random

# 创建数据库连接
conn = MongoClient('localhost',27017)

# 创建数据库对象
db = conn.stu

# 创建集合对象
myset = db.class4
# print(dir(myset))

# *******insert************
# myset.insert_one({'name':'张铁林','King':'乾隆'})
# myset.insert_many([{'name':'张国立','King':'康熙'},
# {'name':'陈道明','King':'康熙王朝'}])
# myset.insert({'name':'唐国强','King':'雍正'})
# myset.insert([{'name':'陈建斌','King':'雍正'},
# {'_id':1,'name':'吴奇隆','King':'四爷'}])
# myset.save({'_id':1,'name':'聂远','King':'乾隆'})

# ********find****************
# cursor = myset.find({'name':{'$exists':True}},{'_id':0})
# for 循环遍历游标得到查找内容
# for i in cursor:
#     # print(i)
#     print(i['name'],'---',i['King'])

# print(cursor.next())

# for i in cursor.skip(2).limit(3):
#     print(i)

# for i in cursor.sort([('name',1),('King',-1)]):
#     print(i)

# cursor = myset.find_one({'$or':[{'name':'陈道明'},{'King':'乾隆'}]},{'_id':0})
# print(cursor['name'],'---',cursor['King'])

# *******update**********
# myset.update_one({'King':'康熙'},{'$set':{'king_name':'玄烨'}})
# myset.update_many({'King':'雍正'},{'$set':{'king_name':'胤禛'}})
# myset.update({'King':'乾隆'},{'$set':{'king_name':'弘历'}},multi=True)

# 插入新文档
# myset.update_one({'name':'郑少秋'},{'$set':{'King':'乾隆'}},upsert=True)

# *******delete*********
# myset.delete_one({'King':'康熙'})
# myset.delete_many({'King':'雍正'})
# myset.remove({'king_name':None})

# ******fuhe*********
# data = myset.find_one_and_delete({'name':'张铁林'})
# print(data)

# ******index******
# myset = db.class1  # 切换使用集合

# 创建正向索引
# index_name = myset.create_index('name')
# 等同于
# index_name = myset.create_index([('name',1)])

# 创建逆向索引
# index_name = myset.create_index([('name',-1)])
# print(index_name)

# 创建age索引改名为Age
# index_name = myset.create_index('age',name='Age')
# print(index_name)

# 创建稀疏索引
# index_name = myset.create_index('name',name='NAME',sparse=True)
# print(index_name)

# 查看索引
# for i in myset.list_indexes():
#     print(i)

# myset.drop_index('NAME')   # 索引名称删除
# myset.drop_index([('name',-1)])   # 键值删除
# myset.drop_indexes()    # 删除所有索引

# *********aggregate************
# l = [{'$group':{'_id':'$sex','num':{'$sum':1}}}]
# cursor = myset.aggregate(l)
# for i in cursor:
#     print(i)

myset = db.class2  # 切换使用集合

# for i in range(9):
#     myset.update_one({'score':{'$exists':False}},{'$set':{'score':{'Chinese':random.randint(60,100),'Math':random.randint(60,100),'English':random.randint(60,100)}}})

cursor = myset.aggregate([{'$group':{'_id':'$sex'}},{'$sort':{'score':1}},{'$project':{'_id':0}}])
for i in cursor:
    print(i)
    
# 关闭数据库连接
conn.close()