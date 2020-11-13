import pprint
import statistics
import numpy as np
import numpy
import xlwt
from matplotlib import pyplot
from pymongo import MongoClient

import Utility

__author__ = 'Abduljaleel Al Rubaye'

final_time_line_db = MongoClient().github_data.final_time_line

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
    mean = numpy.mean(myList)
    std = numpy.std(myList)
    std_minus_one = mean - std
    std_plus_one = mean + std
    count_minus = len([i for i in myList if i < std_minus_one])
    count_mid = len([i for i in myList if std_minus_one < i < std_plus_one])
    count_plus = len([i for i in myList if i > std_plus_one])
    perc_minus = count_minus / len_list
    perc_mid = count_mid / len_list
    perc_plus = count_plus / len_list

    return {
        'dense': count_minus,
        'normal': count_mid,
        'dispersed': count_plus,
        'dense_prc': perc_minus,
        'normal_prc': perc_mid,
        'dispersed_prc': perc_plus
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
        'issues_count': cc-1,
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
        'commits_count': cc-1,
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
    count = final_time_line_db.count()
    k = 0
    for e in final_time_line_db.find():
        try:
            if e.get('time_line'):
                name = e.get('name')
                time_line = e.get('time_line')
                entry = []
                for event in time_line:
                    if event.get('type') == 'IssueOpened' or event.get('type') == 'Commit':
                        entry.append(event)
                if len(entry) > 0:
                    sorted_entry = sorted(entry, key=lambda l: l['created_at'])
                    process_issues_dates(sorted_entry, name)
                    process_commits_between_issues(sorted_entry, name)
                    print 'repo ('+str(k) + ') is done.'
                    results.save("dist_reg.xls")
            k += 1
            # if k > 5:
            #     break
        except Exception as er:
            print '-----'*10
            print er.message
            print '-----'*10
            k += 1
            # if k > 5:
            #     break
