import pprint
from pymongo import MongoClient

__author__ = 'Abdul Rubaye'

client = MongoClient()
database = client.github_data
repos = database.repos
pull_requests = database.pull_requests
events = database.events
commits = database.commits.bson
commit_comments = database.commit_comments

# client id and client secret are used in calling the github API
# they will help to raise the maximum limit of calls per hour
# note: you will need your private txt file that includes the private keys
privateVar = open("privateVar.txt",'r').read()
client_id = privateVar.split('\n', 1)[0]
client_secret = privateVar.split('\n', 1)[1]

# appends the client id and the client secret to urls
def add_client_id_client_secret_to_url(url,page):
    query = '?per_page=100&page='+str(page)+'&client_id='+client_id+'&client_secret='+client_secret
    return url+query

# The main function
if __name__ == "__main__":

    i = 1

    # for e in repos.find():
    #     pprint.pprint(e)
    #     if i > 1:
    #         break
    #     i += 1
    #     print '*'*100

    for e in commit_comments.find():
        pprint.pprint(e)
        break

