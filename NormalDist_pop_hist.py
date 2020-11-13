import pprint
import statistics
import numpy as np
import numpy
import xlwt
from matplotlib import pyplot
from pymongo import MongoClient

import Utility

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


def histogram(myList):
    print '-'*100
    print myList
    mean = np.mean(myList)
    print mean
    pyplot.hist(myList, bins = 10)
    pyplot.show()


def process_issues_dates(ent, repo_name):
    open_issue_date = []
    cc = 0
    for jj in range(0, len(ent)):
        open_issue_date.append(ent[jj]['created_at'])
        cc += 1

    days_between_issues = []

    sorted_issues_time_line = sorted(open_issue_date, key=lambda l: l)

    for dt in range(0, len(sorted_issues_time_line) - 1):
        days_between_issues.append(Utility.time_diff(sorted_issues_time_line[dt], sorted_issues_time_line[dt + 1]))

    histogram(days_between_issues)



if __name__ == "__main__":

    gg = [75852, 21461, 15944, 1994, 12438, 40086, 40301, 11375, 42724, 40049, 40345, 80136, 69402, 29961, 45689, 45231, 33999, 60302, 34599, 55034, 80839, 28199, 62276, 51967, 30635, 60489, 52732, 25721, 49781, 75455, 29496, 42600, 20244, 39105, 60984, 64065, 52840, 52228, 73706, 71504, 23025, 37168, 41431, 43846, 32388, 4, 61746, 5440, 40840, 21000, 16233, 40372, 40648, 48228, 22064, 45344, 83273, 29571, 85282, 47265, 41226, 11342, 53454, 77523, 28640, 40404, 47431, 39098, 26297]
    histogram(gg)
    # for k in range(0, len(db_list)):
    #     try:
    #         count = db_list[k].count()
    #         if count > 0:
    #             main_entry = db_list[k].find()[count - 1]
    #             if main_entry.get('contributors_count'):
    #                 entry = []
    #                 j = 0
    #                 for e in db_list[k].find():
    #                     j += 1
    #                     if not e.get('contributors_count'):
    #                         if e.get('type') == 'IssueOpened':
    #                             entry.append(e)
    #
    #                 sorted_entry = sorted(entry, key=lambda l: l['created_at'])
    #                 process_issues_dates(sorted_entry, e.get('name'))
    #                 print 'repo (' + str(k) + ') is done'
    #             else:
    #                 print str(k) + ' is not a complete processed repository'
    #
    #     except Exception as er:
    #         print er.message
