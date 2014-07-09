__author__ = 'lab_alglam'

#import from main module
from web import admin

from flask import Flask
#Admin
from flask.ext.admin import Admin

#redis CLI
from flask.ext.admin.contrib import rediscli
from classes.redis_kv import redis_kv

admin.add_view(rediscli.RedisCli(redis_kv))
