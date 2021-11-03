import json
import pprint
import time
from pymongo import MongoClient
import urllib
import Utility
import networkx as nx

__author__ = 'Abduljaleel Al Rubaye'

client = MongoClient()
database = client.github_data
repos = database.popular_repo_3


# The main function
if __name__ == "__main__":

    time_line_array = []
    graph = nx.Graph()

    # iterate over the items inside the repos collection and do "what you like to do"
    for item in repos.find():
        try:
            entry = {}
            if item.get('type') == 'Comment':
                x = item['url'].split("/")
                entry = {
                    'created_at' : item['comment_created_at'],
                    'issue_number' : item['issue_number'],
                    'sentiment_label': item['sentient_label'],
                    'type': 'Comment',
                    'comment_number': x[len(x)-1],
                    'name':'Comment_'+ str(x[len(x)-1]),
                    'author': item['author'],
                    'author_followers': item['author_followers_count']
                }
            if item.get('type') == 'IssueOpened':
                entry = {
                    'created_at' : item['created_at'],
                    'comments_count' : item['comments_count'],
                    'seconds_to_close' : item['seconds_to_close'],
                    'issue_number' : item['issue_number'],
                    'type': 'Issue',
                    'name': 'Issue_'+str(item['issue_number'])
                }
            if len(entry) > 0:
                time_line_array.append(entry)
        except Exception as error:
            print error

    sorted_time_line = sorted(time_line_array, key=lambda l: l['created_at'])

    # for i in range (0, len(sorted_time_line)):
    #     obj_name = str(sorted_time_line[i]['name'])
    #     if sorted_time_line[i]['type'] == 'Issue':
    #         graph.add_node(obj_name, name = obj_name, type = "Issue", Issue=str(sorted_time_line[i]['issue_number']), comments_count=sorted_time_line[i]['comments_count'], )
    #     # else:
    #     #     comment_name = "Comment_"+sorted_time_line[i]['comment_number']
    #     #     graph.add_node(obj_name, name = obj_name, type = "Comment", Issue=str(sorted_time_line[i]['issue_number']), comments_count = 0)
    #
    # # time_line_connection
    # for i in range(0, len(sorted_time_line)-1):
    #     node1 = sorted_time_line[i]['name']
    #     node2 = sorted_time_line[i+1]['name']
    #     graph.add_edge(node1, node2, type='time_line')

    sorted_issue = sorted(time_line_array, key=lambda l: ((l['issue_number']), l['created_at']))

    # # issue_comment_connection
    # for i in range(0, len(sorted_issue)):
    #     if sorted_issue[i]['type'] == 'Issue':
    #         node1 = sorted_issue[i]['name']
    #     else:
    #         node2 = sorted_issue[i]['name']
    #         if not graph.has_edge(node1, node2):
    #             graph.add_edge(node1, node2,type='issue_comment', weight = 5)
    #
    # # issue_issue_connection
    # sorted_only_issues = []
    # for i in range(0, len(sorted_issue)):
    #     if sorted_issue[i]['type'] == 'Issue':
    #         sorted_only_issues.append(sorted_issue[i])
    #
    # for i in range(0, len(sorted_only_issues)-1):
    #     node1 = sorted_only_issues[i]['name']
    #     node2 = sorted_only_issues[i+1]['name']
    #     if not graph.has_edge(node1, node2):
    #         graph.add_edge(node1,node2, type='issue_issue', weight = 5)

    # nx.write_graphml(graph, "/Users/Abduljaleel/Desktop/IssuesTimeLine-2.graphml")
    authors = []
    authors_followers = []
    for i in range (0, len(sorted_issue)-1):
        if sorted_issue[i]['type'] == 'Issue':
            unique_authors = set(authors)
            print str(sorted_issue[i]['issue_number']) + "===>" + str(len(authors)) + " : " + str(len(unique_authors))
            authors = []
            authors_followers = []
        else:
            commenter = sorted_issue[i]['author']
            authors.append(commenter)

