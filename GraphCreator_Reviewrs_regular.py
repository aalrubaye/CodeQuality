import pprint
import networkx as nx
from datetime import datetime
from datetime import timedelta
from pymongo import MongoClient
import numpy
import random
import Utility
from scipy.stats import linregress
import xlwt
import numpy as np

__author__ = 'Abduljaleel Al Rubaye'

db_list = MongoClient().github_data.final_time_line

Sheet_first_row = [
    'name',
    'author',
    'author_fc',
    'issues',
    'comments',
    'stars',
    'contributors',
    'popularity-degree-R-val',
    'popularity-degree-P-val',
    'community_score',
    'exp_0.1',
    'exp_0.2',
    'exp_0.3',
    'exp_0.4',
    'exp_0.5',
    'exp_0.6',
    'exp_0.7',
    'exp_0.8',
    'exp_0.9',
    'exp_1',
    'deg_0.1',
    'deg_0.2',
    'deg_0.3',
    'deg_0.4',
    'deg_0.5',
    'deg_0.6',
    'deg_0.7',
    'deg_0.8',
    'deg_0.9',
    'deg_1'
]

# perc_exp_sheet = ['name', 'issues', 'stars', 'contributors', 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

perc_exp = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]


def coeff(a,b):
    r = linregress(a,b)
    return r


def graph_creator():
    results = xlwt.Workbook(encoding="utf-8")
    sheet1 = results.add_sheet('Community_Robustness')
    # sheet2 = results.add_sheet('Experience_Coverage')
    # sheet3 = results.add_sheet('Degree_Coverage')

    col = 0
    row = 0
    for i in range(0, len(Sheet_first_row)):
        sheet1.write(row, col, str(Sheet_first_row[i]))
        col += 1

    # col = 0
    # for i in range(0, len(perc_exp_sheet)):
    #     sheet2.write(row, col, str(perc_exp_sheet[i]))
    #     sheet3.write(row, col, str(perc_exp_sheet[i]))
    #     col += 1
    kkcount = 0
    for e in db_list.find():
        com = 0
        isu = 0
        row += 1
        try:
            if e.get('time_line'):
                time_line = e.get('time_line')
                repo_name = e.get('name')
                # print repo_name
                repo_owner = e.get('owner')
                repo_owner_fc = e.get('owner_followers_count')
                repo_issues_count = e.get('statistics').get('total_issues')
                repo_issues_comments_count = e.get('statistics').get('total_issues_comments')
                repo_stars = e.get('popularity').get('stars')
                repo_contributors = e.get('contributors_count')

                if repo_name == 'ember-cli-tailwind':
                    # print 'yesssssss'

                    if repo_contributors:
                        comments_list = []
                        # main loop
                        i = 0
                        for t in time_line:
                            type = t.get('type')
                            if type != 'Commit':
                                issue_number = t.get('issue_number')
                                author = t.get('author')
                                followers = t.get('author_followers_count')

                                if type == 'IssueOpened':
                                    isu += 1
                                    comments_count = t.get('comments_count')
                                    graph.add_node(issue_number, name=issue_number, n_type=type, author=author, afc=followers, comments_count=comments_count)
                                    comments = t.get('comments')

                                    for c in comments:
                                        comment_author = c.get('author')
                                        comment_author_followers = c.get('author_followers_count')
                                        if comment_author not in comments_list:
                                            com += 1
                                            comments_list.append(comment_author)
                                            graph.add_node(comment_author, name=comment_author, n_type='Comment', author=comment_author, afc=comment_author_followers)
                                        if graph.has_edge(issue_number, comment_author):
                                            graph[issue_number][comment_author]['weight'] += 1
                                        else:
                                            graph.add_edge(issue_number, comment_author, weight=1)

                        popularities = []
                        degrees = []
                        people = []
                        connections = []
                        for n in graph.nodes():
                            node = graph.nodes[n]
                            node_type = node['n_type']

                            if node_type != 'IssueOpened':
                                if graph.degree[n] > 1:
                                    people.append(node['afc'])
                                    connections.append(graph.degree[n])
                                popularities.append(node['afc'])
                                degrees.append(graph.degree(weight='weight')[n])

                        # print graph.nodes()
                        # print '********'

                        if len(popularities) > 0 and len(degrees) > 0:
                            r = coeff(popularities, degrees)
                            r_val = r[2]
                            p_val = r[3]

                            # K-Aug connectivity
                            needed_edges_to_connect = len(sorted(nx.k_edge_augmentation(graph, k=1)))
                            edges_to_connect_full_graph = isu - 1
                            edges = len(graph.edges())
                            community_score = 1.00 - (needed_edges_to_connect/float(edges_to_connect_full_graph))
                            # community_score = 1.00 - (needed_edges_to_connect/float(edges))

                            sum_connection = sum(connections)
                            sum_people = sum(people)

                            sorted_people_connections = sorted(zip(people, connections))
                            # print sorted_people_connections

                            sorted_connections_people = sorted(zip(connections, people))
                            # print sorted_connections_people

                            experience_coverage = []
                            degree_coverage = []

                            if sum_people > 0 and sum_connection > 0 :

                                for kk in range(0, 10):
                                    indexx = int(len(people) * (1-perc_exp[kk]))
                                    sum_exp = 0
                                    sum_deg = 0
                                    if indexx > 0:
                                        indexx -= 1
                                    for jj in range(indexx, len(people)):
                                        sum_exp += sorted_people_connections[jj][1]
                                        sum_deg += sorted_connections_people[jj][1]

                                    experience_coverage.append(sum_exp / float(sum_connection))
                                    degree_coverage.append(sum_deg / float(sum_people))

                                info = [
                                    repo_name,
                                    repo_owner,
                                    repo_owner_fc,
                                    repo_issues_count,
                                    repo_issues_comments_count,
                                    repo_stars,
                                    repo_contributors,
                                    r_val,
                                    p_val,
                                    community_score
                                ]

                                # experience_coverage_sheet = [repo_name,repo_issues_count,repo_stars,repo_contributors]
                                # degree_coverage_sheet = [repo_name,repo_issues_count,repo_stars,repo_contributors]

                                for i in range(0, len(experience_coverage)):
                                    info.append(experience_coverage[i])

                                for i in range(0, len(experience_coverage)):
                                    info.append(degree_coverage[i])

                                col = 0
                                for i in range(0, len(Sheet_first_row)):
                                    sheet1.write(row, col, str(info[i]))
                                    col += 1
                        print 'hiiiiiiiii'
                        nx.write_graphml(graph, "/Users/Abduljaleel/Desktop/net3.graphml")
                        print repo_name
                        graph.clear()
                        break

        except Exception as er:
            graph.clear()
            print er
        #
        # kkcount += 1
        # if kkcount > 50:
        #     break

    # results.save("/Users/Abduljaleel/Desktop/regular_NEW.xls")


if __name__ == "__main__":
    graph = nx.Graph()
    graph_creator()


