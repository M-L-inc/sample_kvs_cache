from dao import connect_redis, connect_db

def charge_redis():
    with connect_db() as db_conn, db_conn.cursor() as cursor:
        cursor.execute('SELECT id,name,age FROM users')
        users = cursor.fetchall()

        TMP_CACHE_KEY = "userinfo_tmp"
        CACHE_KEY = "userinfo"
        print(f"users count: {len(users)}, start charge redis cache")

        with connect_redis() as r_conn:
            for user_id, user_name, user_age in users:
                r_conn.hset(TMP_CACHE_KEY, user_name, f"{user_id},{user_name},{user_age}")

            print("redis cache charge completed")

            # rename userinfo_tmp to userinfo
            r_conn.rename(TMP_CACHE_KEY, CACHE_KEY)

charge_redis()
