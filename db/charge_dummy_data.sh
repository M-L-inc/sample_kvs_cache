#!/bin/sh

# check dummy_data.sql exists
if [ ! -f dummy_data.sql ]; then
    python3 create_dummy_data.py
fi

mysql -u benchmark_user -pbenchmark_test -h localhost myflaskapp < dummy_data.sql