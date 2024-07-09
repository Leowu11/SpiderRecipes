import sqlite3


def writeDb(data):
    # 建立与数据库的连接
    connection = sqlite3.connect('database.db')

    # 创建游标对象
    cursor = connection.cursor()

    # 检查数据表是否存在
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='data'")
    table_exists = cursor.fetchone()

    # 如果数据表不存在，则创建数据表
    if not table_exists:
        cursor.execute("CREATE TABLE data (id INT PRIMARY KEY, name TEXT)")

    # 检查链接表是否存在
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='links'")
    table_exists = cursor.fetchone()

    # 如果链接表不存在，则创建链接表
    if not table_exists:
        cursor.execute("CREATE TABLE links (data_id INT, link TEXT)")

    # 检查操作表是否存在
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='actions'")
    table_exists = cursor.fetchone()

    # 如果操作表不存在，则创建操作表
    if not table_exists:
        cursor.execute("CREATE TABLE actions (data_id INT, action TEXT)")

        # 检查操作表是否存在
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='materials'")
    table_exists = cursor.fetchone()

    # 如果操作表不存在，则创建操作表
    if not table_exists:
        cursor.execute("CREATE TABLE materials (data_id INT, material TEXT)")

    # # 示例数据
    # data = [
    #     {
    #         'id': 1,
    #         'name': 'John',
    #         'links': ['link1', 'link2', 'link3'],
    #         'actions': ['action1', 'action2']
    #     },
    #     {
    #         'id': 2,
    #         'name': 'Jane',
    #         'links': ['link4', 'link5'],
    #         'actions': ['action3', 'action4', 'action5']
    #     },
    #     {
    #         'id': 3,
    #         'name': 'Bob',
    #         'links': ['link6'],
    #         'actions': ['action6', 'action7', 'action8', 'action9']
    #     }
    # ]

    # 插入数据
    for item in data:
        values = (int(item['id']), str(item['name']))
        cursor.execute("INSERT OR IGNORE INTO data (id, name) VALUES (?, ?)", values)

        # data_id = cursor.lastrowid

        for link in item['links']:
            values = (int(item['id']), link)
            cursor.execute("INSERT INTO links (data_id, link) VALUES (?, ?)", values)

        for action in item['actions']:
            values = (int(item['id']), action)
            cursor.execute("INSERT INTO actions (data_id, action) VALUES (?, ?)", values)
        for mate in item['materials']:
            values = (int(item['id']), mate)
            cursor.execute("INSERT INTO materials (data_id, material) VALUES (?, ?)", values)

    connection.commit()
    connection.close()
