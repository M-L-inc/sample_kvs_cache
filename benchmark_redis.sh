#!/bin/sh

#apt install -y apache2-utils
ab -n 100000 -c 500 http://127.0.0.1:8888/redis_get_user

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