import psycopg2
import sql_queries

connection = psycopg2.connect(database='supervisor_bot', user='bot_system', host='localhost', password='system')

cursor = connection.cursor()


def insert_into_bd(message):
    cursor.execute('INSERT INTO bot_table VALUES(%s, %s)', (message.chat.id, message.text))
    connection.commit()


def check_user_id(user_id):
    return False


def get_username_by_id(user_id):
    return None