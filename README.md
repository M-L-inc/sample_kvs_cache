# sample_kvs_cache

# benchmark data

* dummy data: `./db/dummy_data.sql` 10000 rows
* db schema: `db/main.sql`
* application: https://github.com/M-L-inc/sample_kvs_cache/blob/master/main.py#L7-L22

# redis result
command: `./benchmark_redis.sh`

```
# Concurrency Level:      500
# Time taken for tests:   9.060 seconds
# Complete requests:      100000
# Failed requests:        10035
#    (Connect: 0, Receive: 0, Length: 10035, Exceptions: 0)
# Total transferred:      18577794 bytes
# HTML transferred:       3277794 bytes
# Requests per second:    11037.24 [#/sec] (mean)
# Time per request:       45.301 [ms] (mean)
# Time per request:       0.091 [ms] (mean, across all concurrent requests)
# Transfer rate:          2002.42 [Kbytes/sec] received
```

# db resul
command: `./benchmark_db.sh`

```
# Concurrency Level:      500
# Time taken for tests:   32.245 seconds
# Complete requests:      100000
# Failed requests:        9935
#    (Connect: 0, Receive: 0, Length: 9935, Exceptions: 0)
# Total transferred:      18578058 bytes
# HTML transferred:       3278058 bytes
# Requests per second:    3101.22 [#/sec] (mean)
# Time per request:       161.227 [ms] (mean)
# Time per request:       0.322 [ms] (mean, across all concurrent requests)
# Transfer rate:          562.64 [Kbytes/sec] received
```
