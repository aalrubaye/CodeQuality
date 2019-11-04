import pprint

from pymongo import MongoClient

__author__ = 'Abdul Rubaye'

client = MongoClient()
database = client.github_data
repos = database.repos


# The main function
if __name__ == "__main__":

    for e in repos.find():
        pprint.pprint(e)
        break
