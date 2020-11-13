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

Issue_Sheet_first_row = [
    'repo_name',
    'issues_count',
    'dense_issues',
    'normal_issues',
    'dispersed_issues',
    'dense_issues_prc',
    'normal_issues_prc',
    'dispersed_issues_prc'
]

Commit_Sheet_first_row = [
    'repo_name',
    'commits_count',
    'dense_commits',
    'normal_commits',
    'dispersed_commits',
    'dense_commits_prc',
    'normal_commits_prc',
    'dispersed_commits_prc'
]


def distribution(myList):
    len_list = float(len(myList))

    q1 = numpy.percentile(myList, 25)
    q2 = numpy.median(myList)

    normal_limit = (2 * q2) - q1

    below_normal_issues_count = len([i for i in myList if i < q1])
    normal_issues_count = len([i for i in myList if q1 < i < normal_limit])
    above_normal_issues_count = len([i for i in myList if i > normal_limit])

    below_normal_issues_count_prc = below_normal_issues_count / len_list
    normal_issues_count_prc = normal_issues_count / len_list
    above_normal_issues_count_prc = above_normal_issues_count / len_list

    return {
        'dense': below_normal_issues_count,
        'normal': normal_issues_count,
        'dispersed': above_normal_issues_count,
        'dense_prc': below_normal_issues_count_prc,
        'normal_prc': normal_issues_count_prc,
        'dispersed_prc': above_normal_issues_count_prc
    }


def export_to_sheet1(entry, sheet):
    global row_issue
    row_issue += 1
    col = 0
    for i in range(0, len(entry)):
        sheet.write(row_issue, col, str(entry[Issue_Sheet_first_row[i]]))
        col += 1


def export_to_sheet2(entry, sheet):
    global row_commits
    row_commits += 1
    col = 0
    for i in range(0, len(entry)):
        sheet.write(row_commits, col, str(entry[Commit_Sheet_first_row[i]]))
        col += 1


def process_issues_dates(ent, repo_name):
    global sheet1
    open_issue_date = []
    cc = 0
    for jj in range(0, len(ent)):
        if ent[jj]['type'] == 'IssueOpened':
            open_issue_date.append(ent[jj]['created_at'])
            cc += 1

    days_between_issues = []

    sorted_issues_time_line = sorted(open_issue_date, key=lambda l: l)

    for dt in range(0, len(sorted_issues_time_line) - 1):
        days_between_issues.append(Utility.time_diff(sorted_issues_time_line[dt], sorted_issues_time_line[dt + 1]))

    dist = distribution(days_between_issues)

    issues_result_entry = {
        'repo_name': repo_name,
        'issues_count': cc - 1,
        'dense_issues': dist['dense'],
        'normal_issues': dist['normal'],
        'dispersed_issues': dist['dispersed'],
        'dense_issues_prc': dist['dense_prc'],
        'normal_issues_prc': dist['normal_prc'],
        'dispersed_issues_prc': dist['dispersed_prc']
    }

    export_to_sheet1(issues_result_entry, sheet1)


def process_commits_between_issues(ent, repo_name):
    global sheet2
    commits = 0
    commits_array = []
    cc = 0
    for jj in range(0, len(ent)):
        if ent[jj]['type'] == 'Commit':
            commits += 1
            cc += 1
        if ent[jj]['type'] == 'IssueOpened':
            commits_array.append(commits)
            commits = 0

    del commits_array[0]
    dist = distribution(commits_array)

    commits_result_entry = {
        'repo_name': repo_name,
        'commits_count': cc - 1,
        'dense_commits': dist['dense'],
        'normal_commits': dist['normal'],
        'dispersed_commits': dist['dispersed'],
        'dense_commits_prc': dist['dense_prc'],
        'normal_commits_prc': dist['normal_prc'],
        'dispersed_commits_prc': dist['dispersed_prc']
    }

    export_to_sheet2(commits_result_entry, sheet2)


def define_xls():
    global row_commits, row_issue, sheet1, sheet2, results
    row_issue = 0
    row_commits = 0
    results = xlwt.Workbook(encoding="utf-8")
    sheet1 = results.add_sheet('Issues')
    sheet2 = results.add_sheet('Commits')

    col = 0
    for i in range(0, len(Issue_Sheet_first_row)):
        sheet1.write(row_issue, col, str(Issue_Sheet_first_row[i]))
        col += 1

    col = 0
    for i in range(0, len(Commit_Sheet_first_row)):
        sheet2.write(row_commits, col, str(Commit_Sheet_first_row[i]))
        col += 1


if __name__ == "__main__":

    global results
    define_xls()

    for k in range(0, len(db_list)):
        try:
            count = db_list[k].count()
            if count > 0:
                main_entry = db_list[k].find()[count - 1]
                if main_entry.get('contributors_count'):
                    entry = []
                    j = 0
                    for e in db_list[k].find():
                        j += 1
                        if not e.get('contributors_count'):
                            if e.get('type') == 'IssueOpened' or e.get('type') == 'Commit':
                                entry.append(e)

                    sorted_entry = sorted(entry, key=lambda l: l['created_at'])
                    process_issues_dates(sorted_entry, e.get('name'))
                    # process_commits_between_issues(sorted_entry, e.get('name'))
                    print 'repo (' + str(k) + ') is done'
                    results.save("dist_pop.xls")
                else:
                    print str(k) + ' is not a complete processed repository'

        except Exception as er:
            print er.message
