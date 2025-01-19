import redis
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='benchmark_user',
        password='benchmark_test',
        database='myflaskapp'
    )

def connect_redis():
    return redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
