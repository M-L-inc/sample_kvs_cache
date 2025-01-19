from flask import Flask
import random
from dao import connect_db, connect_redis

app = Flask(__name__)
conn = connect_db()
r_conn = connect_redis()

@app.route('/db_get_user')
def db_get_user():
    with connect_db() as conn, conn.cursor() as cursor:
        rand_id = random.randint(1, 10000)
        rand_username = f"User{rand_id}"
        cursor.execute('SELECT id, name, age FROM users WHERE name = %s', (rand_username,))
        user = cursor.fetchone()
        return f"id: {user[0]}, name: {user[1]}, age: {user[2]}"

@app.route('/redis_get_user')
def redis_get_user():
    with connect_redis() as r_conn:
        rand_username = f"User{random.randint(1, 10000)}"
        raw_user_data = r_conn.hget("userinfo", rand_username)
        user_id, user_name, user_age = raw_user_data.split(",")
        return f"id: {user_id}, name: {user_name}, age: {user_age}"

@app.route('/ping')
def ping():
    conn = connect_db()
    r_conn = connect_redis()
    if conn.is_connected() and r_conn.ping():
        return 'pong'
    else:
        return 'failed'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=True)