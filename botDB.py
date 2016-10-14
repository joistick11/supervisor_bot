import psycopg2

connection = psycopg2.connect(database='supervisor_bot', user='bot_system', host='localhost', password='system')

cursor = connection.cursor()


def store_message(message_id, user_id, datetime, message_data):
    cursor.execute('INSERT INTO messages VALUES(%s, %s, to_timestamp(%s), %s)',
                   (message_id, user_id, datetime, message_data))
    connection.commit()


def store_new_user_into_db(id, username, first_name, last_name):
    cursor.execute('INSERT INTO users VALUES(%s, %s, %s, %s)', (id, username, first_name, last_name))
    connection.commit()


def check_user_id_exists(id: int) -> bool:
    cursor.execute('SELECT * FROM users WHERE id = %s', [id])
    result = cursor.fetchone()
    if result is not None:
        return True
    else:
        return False
