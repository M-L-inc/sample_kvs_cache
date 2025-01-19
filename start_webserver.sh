#!/bin/sh

gunicorn main:app -w 8 -b 127.0.0.1:8888 --reload
