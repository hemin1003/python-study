import pymysql

db = pymysql.connect(
    host='localhost',
    port = 3306,
    user='root',
    passwd='123456',
    db ='test')

cursor = db.cursor()

# 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭连接
db.close()