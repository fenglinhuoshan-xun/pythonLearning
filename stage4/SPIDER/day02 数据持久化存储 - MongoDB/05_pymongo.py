"""
    python与MongoDB交互
    库名：testdb
    集合名：testset
    文档：{'name':'雄霸','tools':'三分归元气'}
"""

import pymongo

# 1. 创建数据库连接对象
conn = pymongo.MongoClient('localhost', 27017)
# 2. 创建库对象
db = conn['testdb']
# 3. 创建集合对象
myset = db['testset']
# 4. 插入文档
myset.insert_one({'name': '雄霸', 'tools': '三分归元气'})


