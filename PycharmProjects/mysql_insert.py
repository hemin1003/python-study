import pymysql

db = pymysql.connect(
    host='localhost',
    port = 3306,
    user='root',
    passwd='123456',
    db ='test')

cursor = db.cursor()

sql = """
    INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)
"""

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()