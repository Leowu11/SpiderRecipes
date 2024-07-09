import sqlite3

# connection = sqlite3.connect('database.db')
#
# cursor = connection.cursor()
# table_name = ["name", "links", "actions"]
# for table_name in table_name:
#     print("lisname:", table_name)
#     cursor.execute(f"SELECT * FROM {table_name}")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
#     print()
# connection.close()
connection = sqlite3.connect('database.db')
# 创建游标对象
cursor = connection.cursor()
# 查询链接表数据
cursor.execute("SELECT * FROM actions")
links_rows = cursor.fetchall()
# 输出链接表数据 print("链接表数据:")
for row in links_rows:
    data_id, links = row
    print("Data ID:", data_id)
    print("Link:", links)
    # print("actions:", action)
    print()
# 查询数据表数据
cursor.execute("SELECT * FROM data")
data_rows = cursor.fetchall()
# 输出数据表数据 print("数据表数据:")
for row in data_rows:
    id, name = row
    print("ID:", id)
    print("Name:", name)
    print()
# 关闭数据库连接
connection.close()
