#!/bin/sh

#apt install -y apache2-utils
ab -n 100000 -c 500 http://127.0.0.1:8888/db_get_user

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