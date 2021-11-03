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

# db_list = [
#     MongoClient().github_data.popular_repo_1,
#     MongoClient().github_data.popular_repo_2,
#     MongoClient().github_data.popular_repo_3,
#     MongoClient().github_data.popular_repo_4,
#     MongoClient().github_data.popular_repo_5,
#     MongoClient().github_data.popular_repo_6,
#     MongoClient().github_data.popular_repo_7,
#     MongoClient().github_data.popular_repo_8,
#     MongoClient().github_data.popular_repo_9,
#     MongoClient().github_data.popular_repo_10,
#     MongoClient().github_data.popular_repo_11,
#     MongoClient().github_data.popular_repo_12,
#     MongoClient().github_data.popular_repo_13,
#     MongoClient().github_data.popular_repo_14,
#     MongoClient().github_data.popular_repo_15,
#     MongoClient().github_data.popular_repo_16,
#     MongoClient().github_data.popular_repo_17,
#     MongoClient().github_data.popular_repo_18,
#     MongoClient().github_data.popular_repo_19,
#     MongoClient().github_data.popular_repo_20,
#     MongoClient().github_data.popular_repo_21,
#     MongoClient().github_data.popular_repo_22,
#     MongoClient().github_data.popular_repo_23,
#     MongoClient().github_data.popular_repo_24,
#     MongoClient().github_data.popular_repo_25,
#     MongoClient().github_data.popular_repo_26,
#     MongoClient().github_data.popular_repo_27,
#     MongoClient().github_data.popular_repo_28,
#     MongoClient().github_data.popular_repo_29,
#     MongoClient().github_data.popular_repo_30,
#     MongoClient().github_data.popular_repo_31,
#     MongoClient().github_data.popular_repo_32,
#     MongoClient().github_data.popular_repo_33,
#     MongoClient().github_data.popular_repo_34,
#     MongoClient().github_data.popular_repo_35,
#     MongoClient().github_data.popular_repo_36,
#     MongoClient().github_data.popular_repo_37,
#     MongoClient().github_data.popular_repo_38,
#     MongoClient().github_data.popular_repo_39,
#     MongoClient().github_data.popular_repo_40,
#     MongoClient().github_data.popular_repo_41,
#     MongoClient().github_data.popular_repo_42,
#     MongoClient().github_data.popular_repo_43,
#     MongoClient().github_data.popular_repo_44,
#     MongoClient().github_data.popular_repo_45,
#     MongoClient().github_data.popular_repo_46,
#     MongoClient().github_data.popular_repo_47,
#     MongoClient().github_data.popular_repo_48,
#     MongoClient().github_data.popular_repo_49,
#     MongoClient().github_data.popular_repo_50,
#     MongoClient().github_data.popular_repo_51,
#     MongoClient().github_data.popular_repo_52,
#     MongoClient().github_data.popular_repo_53,
#     MongoClient().github_data.popular_repo_54,
#     MongoClient().github_data.popular_repo_55,
#     MongoClient().github_data.popular_repo_56,
#     MongoClient().github_data.popular_repo_57,
#     MongoClient().github_data.popular_repo_58,
#     MongoClient().github_data.popular_repo_59,
#     MongoClient().github_data.popular_repo_60,
#     MongoClient().github_data.popular_repo_61,
#     MongoClient().github_data.popular_repo_62,
#     MongoClient().github_data.popular_repo_63,
#     MongoClient().github_data.popular_repo_64,
#     MongoClient().github_data.popular_repo_65,
#     MongoClient().github_data.popular_repo_66,
#     MongoClient().github_data.popular_repo_67,
#     MongoClient().github_data.popular_repo_68,
#     MongoClient().github_data.popular_repo_69,
#     MongoClient().github_data.popular_repo_70,
#     MongoClient().github_data.popular_repo_71,
#     MongoClient().github_data.popular_repo_72,
#     MongoClient().github_data.popular_repo_73,
#     MongoClient().github_data.popular_repo_74,
#     MongoClient().github_data.popular_repo_75,
#     MongoClient().github_data.popular_repo_76,
#     MongoClient().github_data.popular_repo_77,
#     MongoClient().github_data.popular_repo_78,
#     MongoClient().github_data.popular_repo_79,
#     MongoClient().github_data.popular_repo_80,
#     MongoClient().github_data.popular_repo_81,
#     MongoClient().github_data.popular_repo_82,
#     MongoClient().github_data.popular_repo_83,
#     MongoClient().github_data.popular_repo_84,
#     MongoClient().github_data.popular_repo_85,
#     MongoClient().github_data.popular_repo_86,
#     MongoClient().github_data.popular_repo_87,
#     MongoClient().github_data.popular_repo_88,
#     MongoClient().github_data.popular_repo_89,
#     MongoClient().github_data.popular_repo_90,
#     MongoClient().github_data.popular_repo_91,
#     MongoClient().github_data.popular_repo_92,
#     MongoClient().github_data.popular_repo_93,
#     MongoClient().github_data.popular_repo_94,
#     MongoClient().github_data.popular_repo_95,
#     MongoClient().github_data.popular_repo_96,
#     MongoClient().github_data.popular_repo_97,
#     MongoClient().github_data.popular_repo_98,
#     MongoClient().github_data.popular_repo_99,
#     MongoClient().github_data.popular_repo_100,
#     MongoClient().github_data.popular_repo_101,
#     MongoClient().github_data.popular_repo_102,
#     MongoClient().github_data.popular_repo_103,
#     MongoClient().github_data.popular_repo_104,
#     MongoClient().github_data.popular_repo_105,
#     MongoClient().github_data.popular_repo_106,
#     MongoClient().github_data.popular_repo_107,
#     MongoClient().github_data.popular_repo_108,
#     MongoClient().github_data.popular_repo_109,
#     MongoClient().github_data.popular_repo_110
# ]

db_list = [
    MongoClient().github_data.popular_repo_4
]

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
    'community_score'
]

perc_exp_sheet = ['name', 'issues', 'stars', 'contributors', 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

perc_exp = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

def coeff(a,b):
    r = linregress(a,b)
    return r


def graph_creator():
    results = xlwt.Workbook(encoding="utf-8")
    sheet1 = results.add_sheet('Community_Robustness')
    sheet2 = results.add_sheet('Experience_Coverage')
    sheet3 = results.add_sheet('Degree_Coverage')

    col = 0
    row = 0
    for i in range(0, len(Sheet_first_row)):
        sheet1.write(row, col, str(Sheet_first_row[i]))
        col += 1

    col = 0
    for i in range(0, len(perc_exp_sheet)):
        sheet2.write(row, col, str(perc_exp_sheet[i]))
        sheet3.write(row, col, str(perc_exp_sheet[i]))
        col += 1

    for db in db_list:
        com = 0
        isu = 0
        row += 1
        try:
            count = db.count()
            if count > 0:
                main_entry = db.find()[count - 1]
                repo_name = main_entry.get('name')
                repo_owner = main_entry.get('owner')
                repo_owner_fc = main_entry.get('owner_followers_count')
                repo_issues_count = main_entry.get('statistics').get('total_issues')
                repo_issues_comments_count = main_entry.get('statistics').get('total_issues_comments')
                repo_stars = main_entry.get('popularity').get('stars')
                repo_contributors = main_entry.get('contributors_count')

                if repo_contributors:
                    comments_list = []
                    # main loop
                    i = 0
                    for e in db.find():
                        type = e.get('type')
                        if not e.get('contributors_count') and type != 'Commit':
                            issue_number = e.get('issue_number')
                            author = e.get('author')
                            followers = e.get('author_followers_count')

                            if type == 'IssueOpened':
                                isu += 1
                                comments = e.get('comments_count')
                                graph.add_node(issue_number, name=issue_number, n_type=type, author=author, afc=followers, comments_count=comments)
                        # i += 1
                        # if i>10:
                        #     break

                    #2ndloop
                    i = 0
                    for e in db.find():
                        type = e.get('type')
                        if not e.get('contributors_count') and type != 'Commit':
                            issue_number = e.get('issue_number')
                            author = e.get('author')
                            followers = e.get('author_followers_count')
                            if type == 'Comment':
                                if author not in comments_list:
                                    com += 1
                                    comments_list.append(author)
                                    graph.add_node(author, name=author, n_type=type, author=author, afc=followers)
                                if graph.has_edge(issue_number, author):
                                    graph[issue_number][author]['weight'] += 1
                                else:
                                    graph.add_edge(issue_number, author, weight=1)
                        # i += 1
                        # if i>10:
                        #     break

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

                    r = coeff(popularities, degrees)
                    r_val = r[2]
                    p_val = r[3]

                    # K-Aug connectivity
                    needed_edges_to_connect = len(sorted(nx.k_edge_augmentation(graph, k=1)))
                    edges_to_connect_full_graph = isu - 1
                    edges = len(graph.edges())
                    community_score = 1.00 - (needed_edges_to_connect/float(edges_to_connect_full_graph))
                    # community_score = 1.00 - (needed_edges_to_connect/float(edges))

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

                    col = 0
                    for i in range(0, len(Sheet_first_row)):
                        sheet1.write(row, col, str(info[i]))
                        col += 1

                    sum_connection = sum(connections)
                    sum_people = sum(people)

                    sorted_people_connections = sorted(zip(people, connections))
                    # print sorted_people_connections

                    sorted_connections_people = sorted(zip(connections, people))
                    # print sorted_connections_people

                    experience_coverage = []
                    degree_coverage = []

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

                    experience_coverage_sheet = [repo_name,repo_issues_count,repo_stars,repo_contributors]
                    degree_coverage_sheet = [repo_name,repo_issues_count,repo_stars,repo_contributors]

                    for i in range(0, len(experience_coverage)):
                        experience_coverage_sheet.append(experience_coverage[i])
                        degree_coverage_sheet.append(degree_coverage[i])

                    col = 0
                    for i in range(0, len(perc_exp_sheet)):
                        sheet2.write(row, col, str(experience_coverage_sheet[i]))
                        sheet3.write(row, col, str(degree_coverage_sheet[i]))
                        col += 1

                    print repo_name
                    nx.write_graphml(graph, "/Users/Abduljaleel/Desktop/net1.graphml")
                    graph.clear()
                    break
        except Exception as er:
            graph.clear()
            print er.message

    # results.save("/Users/Abduljaleel/Desktop/popular_new_score3.xls")


if __name__ == "__main__":

    graph = nx.Graph()
    graph_creator()


