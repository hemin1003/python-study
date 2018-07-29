import pymysql

db = pymysql.connect(
    host='localhost',
    port = 3306,
    user='root',
    passwd='123456',
    db ='test')

cursor = db.cursor()

# SEX 为 'M' 的 AGE 字段递增 1
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()