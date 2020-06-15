from pymongo import MongoClient
import pprint

__author__ = 'Abdul'

client = MongoClient()
database = client.github_data
repos = database.repos

# The main function
if __name__ == "__main__":

    # to make sure my converted collection is not empty
    print repos.count()

    # iterate over the items inside the repos collection and do "what you like to do"
    for item in repos.find():
        try:
            # print the whole object
            pprint.pprint(item)

            #OR
            # print a specific field of each data object.
            # for instance if I want to get access to the repository name
            print item['name']

        except Exception as error:
            print error
