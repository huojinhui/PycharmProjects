import pymysql
data = [
    {'姓名': '张三', '性别': '男', '年龄': 20, '身高': 180},
    {'姓名': '张三', '性别': '男', '年龄': 18, '身高': 160},
    {'姓名': '王五', '性别': '男', '年龄': 23, '身高': 150},
    {'姓名': '赵六', '性别': '女', '年龄': 25, '身高': 190},
    {'姓名': '田七', '性别': '男', '年龄': 21, '身高': 170}
]
db = pymysql.connect('localhost', 'root', '', '123')
cursor = db.cursor()
for i in data:
    sql = "INSERT INTO zhanku (url,title,type,fans) VALUES ('%s','%s','%s','%s')" %(i['姓名'], i['性别'], i['年龄'], i['身高'])
    cursor.execute(sql)
db.commit()
