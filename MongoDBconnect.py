from pymongo import MongoClient

__author__ = 'Abdul Rubaye'

client = MongoClient()
database = client.githubData
events = database.events
final_db = database.final
