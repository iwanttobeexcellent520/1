import pymysql

# 连接数据库
db = pymysql.connect(
    host="localhost",
    user="root",
    password="wxk12345",
    database="world"
)

# 创建游标对象
cursor = db.cursor()

# 执行查询语句
# zh=zhanghao

s='2001'
sql_select = f"select * from test where zz={s}"
# sql_select.format(s)
sql_delete="delete from test where age>50"
sql_insert="insert into test (name,age) value ('xikai',21)"

# where between and not in * asc desc
# SELECT CountryCode,District FROM city where ID BETWEEN 1 and 50
# delete from test where
# insert into test (name,age) value ('wxk',21)

cursor.execute(sql_select)
db.commit()

# 获取查询结果
result = cursor.fetchall()
for row in result:
    print(row)


# 关闭游标和数据库连接
cursor.close()
db.close()