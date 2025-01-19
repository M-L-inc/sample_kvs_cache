from dao import connect_redis, connect_db

def charge_redis():
    db_conn = connect_db()
    cursor = db_conn.cursor()
    cursor.execute('SELECT id,name,age FROM users')
    users = cursor.fetchall()

    CACHE_KEY = "userinfo"

    print(f"users count: {len(users)}, start charge redis cache")
    r_conn = connect_redis()
    for user in users:
        user_id, user_name, user_age = user[0], user[1], user[2]
        cache_value = f"{user_id},{user_name},{user_age}"
        r_conn.hset(CACHE_KEY, user_name, cache_value)
    
    print(f"redis cache charge completed")

    cursor.close()
    db_conn.close()

charge_redis()