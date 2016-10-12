import psycopg2


class DB:
    connection = None

    def __init__(self):
        connecttion = psycopg2.connect(database='bot_db', user='bot_user', host='localhost', password='bot_pass123')


cursor = DB.connection.cursor()


def insert_into_bd(message):
    cursor.execute('INSERT INTO bot_table VALUES(%s, %s)', (message.chat.id, message.text))
    DB.connection.commit()
