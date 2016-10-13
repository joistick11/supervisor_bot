import psycopg2
import sql_queries

connection = psycopg2.connect(database='bot_db', user='bot_user', host='localhost', password='bot_pass123')

cursor = connection.cursor()


def insert_into_bd(message):
    cursor.execute(, (message.chat.id, message.text))
    connection.commit()
