import sqlite3

# 打开或创建数据库文件
conn = sqlite3.connect("test.db")

print("打开数据库......")

# 获取游标
c = conn.cursor()

sql = '''
    create table compang


'''
# 执行SQL
c.execute(sql)

# 提交数据库操作
conn.commit()
# 关闭数据库连接
conn.close()

print("建表.......")
