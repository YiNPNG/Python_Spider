from pymongo import MongoClient
from random import randint

conn = MongoClient('localhost',27017)
db = conn.stu
myset = db.class2

cursor = myset.find()

for i in cursor:
    dic = {'Chinese':randint(60,100),'Math':randint(60,100),'English':randint(60,100)}
    myset.update_one({'_id':i['_id']},{'$set':{'score':dic}})

l = [{'$match':{'sex':'m'}},{'$sort':{'score.English':-1}},{'$project':{'_id':0}}]
cursor = myset.aggregate(l)
for i in cursor:
    print(i)

conn.close()