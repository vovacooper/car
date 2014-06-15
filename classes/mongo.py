__author__ = 'vovacooper'

from config import *
from pymongo import MongoClient

db = MongoClient(DATABADE_MONGO_SERVER, tz_aware=True)
