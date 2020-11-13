import pprint
import statistics
import numpy as np
import numpy
import xlwt
from matplotlib import pyplot
from pymongo import MongoClient
import Utility
import networkx as nx

__author__ = 'Abduljaleel Al Rubaye'

db_list = [
    MongoClient().github_data.popular_repo_1,
    MongoClient().github_data.popular_repo_2,
    MongoClient().github_data.popular_repo_3,
    MongoClient().github_data.popular_repo_4,
    MongoClient().github_data.popular_repo_5,
    MongoClient().github_data.popular_repo_6,
    MongoClient().github_data.popular_repo_7,
    MongoClient().github_data.popular_repo_8,
    MongoClient().github_data.popular_repo_9,
    MongoClient().github_data.popular_repo_10,
    MongoClient().github_data.popular_repo_11,
    MongoClient().github_data.popular_repo_12,
    MongoClient().github_data.popular_repo_13,
    MongoClient().github_data.popular_repo_14,
    MongoClient().github_data.popular_repo_15,
    MongoClient().github_data.popular_repo_16,
    MongoClient().github_data.popular_repo_17,
    MongoClient().github_data.popular_repo_18,
    MongoClient().github_data.popular_repo_19,
    MongoClient().github_data.popular_repo_20,
    MongoClient().github_data.popular_repo_21,
    MongoClient().github_data.popular_repo_22,
    MongoClient().github_data.popular_repo_23,
    MongoClient().github_data.popular_repo_24,
    MongoClient().github_data.popular_repo_25,
    MongoClient().github_data.popular_repo_26,
    MongoClient().github_data.popular_repo_27,
    MongoClient().github_data.popular_repo_28,
    MongoClient().github_data.popular_repo_29,
    MongoClient().github_data.popular_repo_30,
    MongoClient().github_data.popular_repo_31,
    MongoClient().github_data.popular_repo_32,
    MongoClient().github_data.popular_repo_33,
    MongoClient().github_data.popular_repo_34,
    MongoClient().github_data.popular_repo_35,
    MongoClient().github_data.popular_repo_36,
    MongoClient().github_data.popular_repo_37,
    MongoClient().github_data.popular_repo_38,
    MongoClient().github_data.popular_repo_39,
    MongoClient().github_data.popular_repo_40,
    MongoClient().github_data.popular_repo_41,
    MongoClient().github_data.popular_repo_42,
    MongoClient().github_data.popular_repo_43,
    MongoClient().github_data.popular_repo_44,
    MongoClient().github_data.popular_repo_45,
    MongoClient().github_data.popular_repo_46,
    MongoClient().github_data.popular_repo_47,
    MongoClient().github_data.popular_repo_48,
    MongoClient().github_data.popular_repo_49,
    MongoClient().github_data.popular_repo_50,
    MongoClient().github_data.popular_repo_51,
    MongoClient().github_data.popular_repo_52,
    MongoClient().github_data.popular_repo_53,
    MongoClient().github_data.popular_repo_54,
    MongoClient().github_data.popular_repo_55,
    MongoClient().github_data.popular_repo_56,
    MongoClient().github_data.popular_repo_57,
    MongoClient().github_data.popular_repo_58,
    MongoClient().github_data.popular_repo_59,
    MongoClient().github_data.popular_repo_60,
    MongoClient().github_data.popular_repo_61,
    MongoClient().github_data.popular_repo_62,
    MongoClient().github_data.popular_repo_63,
    MongoClient().github_data.popular_repo_64,
    MongoClient().github_data.popular_repo_65,
    MongoClient().github_data.popular_repo_66,
    MongoClient().github_data.popular_repo_67,
    MongoClient().github_data.popular_repo_68,
    MongoClient().github_data.popular_repo_69,
    MongoClient().github_data.popular_repo_70,
    MongoClient().github_data.popular_repo_71,
    MongoClient().github_data.popular_repo_72,
    MongoClient().github_data.popular_repo_73,
    MongoClient().github_data.popular_repo_74,
    MongoClient().github_data.popular_repo_75,
    MongoClient().github_data.popular_repo_76,
    MongoClient().github_data.popular_repo_77,
    MongoClient().github_data.popular_repo_78,
    MongoClient().github_data.popular_repo_79,
    MongoClient().github_data.popular_repo_80,
    MongoClient().github_data.popular_repo_81,
    MongoClient().github_data.popular_repo_82,
    MongoClient().github_data.popular_repo_83,
    MongoClient().github_data.popular_repo_84,
    MongoClient().github_data.popular_repo_85,
    MongoClient().github_data.popular_repo_86,
    MongoClient().github_data.popular_repo_87,
    MongoClient().github_data.popular_repo_88,
    MongoClient().github_data.popular_repo_89,
    MongoClient().github_data.popular_repo_90,
    MongoClient().github_data.popular_repo_91,
    MongoClient().github_data.popular_repo_92,
    MongoClient().github_data.popular_repo_93,
    MongoClient().github_data.popular_repo_94,
    MongoClient().github_data.popular_repo_95,
    MongoClient().github_data.popular_repo_96,
    MongoClient().github_data.popular_repo_97,
    MongoClient().github_data.popular_repo_98,
    MongoClient().github_data.popular_repo_99,
    MongoClient().github_data.popular_repo_100,
    MongoClient().github_data.popular_repo_101,
    MongoClient().github_data.popular_repo_102,
    MongoClient().github_data.popular_repo_103,
    MongoClient().github_data.popular_repo_104,
    MongoClient().github_data.popular_repo_105,
    MongoClient().github_data.popular_repo_106,
    MongoClient().github_data.popular_repo_107,
    MongoClient().github_data.popular_repo_108,
    MongoClient().github_data.popular_repo_109,
    MongoClient().github_data.popular_repo_110
]



if __name__ == "__main__":

    graph = nx.Graph()
    a = [[], [], [], [], [], [], [], [], [], [], [], []]
    c = [[], [], [], [], [], [], [], [], [], []]
    current_lang = []
    lang_ind = 0
    lang_log = []
    for k in range(0, len(db_list)):
        try:
            count = db_list[k].count()
            if count > 0:
                main_entry = db_list[k].find()[count - 1]

                age = Utility.repos_age(main_entry.get('created_at'))
                issues = main_entry.get('statistics').get('total_issues')
                closed = main_entry.get('statistics').get('total_closed_issues')
                commits = main_entry.get('statistics').get('total_commits')
                comments = main_entry.get('statistics').get('total_issues_comments')
                name = main_entry.get('name')
                lang = main_entry.get('language')

                issues_per_day = issues / float(age)
                days_to_new_issue = age / float(issues)
                closed_issue_ratio = closed / float(issues)
                commits_to_issues_ratio = commits / float(issues)
                comments_per_issues = comments / float(issues)

                issue_range = [1,2,4,7,10,15,30,60,90,180,365,730]
                if days_to_new_issue > 730:
                    j2 = [730]
                else:
                    j2 = [i for i in issue_range if i >= days_to_new_issue]
                index = 12 - len(j2)
                a[index].append(name)

                close_index = int(closed_issue_ratio * 10)

                if close_index == 10:
                    close_index = 9
                c[close_index].append(name)

                graph.add_node(name, name=name, lang=lang, group=index)
                # graph.add_node(name, name=name, lang=lang, group=index, closed=int(closed_issue_ratio * 10))

                if lang not in lang_log:
                    current_lang.append({
                        'lang': lang,
                        'index': lang_ind
                    })
                    lang_log.append(lang)
                    lang_ind += 1

                # filter(lambda person: person['lang'] == lang, current_lang)

        except Exception as er:
            print er.message

    l = []
    for i in range(0, len(current_lang)):
        l.append([])

    for (p, d) in graph.nodes(data=True):
        lang = d['lang']
        name = d['name']
        index = filter(lambda person: person['lang'] == lang, current_lang)[0]['index']
        l[index].append(name)

    # edges between issue related repos
    for entry in a:
        for i in range (0, len(entry)):
            for j in range(i+1, len(entry)):
                node1 = entry[i]
                node2 = entry[j]
                graph.add_edge(node1, node2, weight=1)

    # edges between language related repos
    for entry in l:
        for i in range (0, len(entry)):
            for j in range (0, len(entry)):
                node1 = entry[i]
                node2 = entry[j]

                if graph.has_edge(node1, node2):
                    graph[node1][node2]['weight'] += 10
                else:
                    graph.add_edge(node1, node2, weight=1)

    # # edges between closed issues related repos
    # for entry in c:
    #     for i in range(0, len(entry)):
    #         for j in range(0, len(entry)):
    #             node1 = entry[i]
    #             node2 = entry[j]
    #
    #             if graph.has_edge(node1, node2):
    #                 graph[node1][node2]['weight'] += 10
    #             else:
    #                 graph.add_edge(node1, node2, weight=1)

    nx.write_graphml(graph, "/Users/Abduljaleel/Desktop/issueGraph_popular.graphml")
