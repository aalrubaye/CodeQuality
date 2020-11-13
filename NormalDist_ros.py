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
MongoClient().github_data.ros_repo_1,
MongoClient().github_data.ros_repo_2,
MongoClient().github_data.ros_repo_3,
MongoClient().github_data.ros_repo_4,
MongoClient().github_data.ros_repo_5,
MongoClient().github_data.ros_repo_6,
MongoClient().github_data.ros_repo_7,
MongoClient().github_data.ros_repo_8,
MongoClient().github_data.ros_repo_9,
MongoClient().github_data.ros_repo_10,
MongoClient().github_data.ros_repo_11,
MongoClient().github_data.ros_repo_12,
MongoClient().github_data.ros_repo_13,
MongoClient().github_data.ros_repo_14,
MongoClient().github_data.ros_repo_15,
MongoClient().github_data.ros_repo_16,
MongoClient().github_data.ros_repo_17,
MongoClient().github_data.ros_repo_18,
MongoClient().github_data.ros_repo_19,
MongoClient().github_data.ros_repo_20,
MongoClient().github_data.ros_repo_21,
MongoClient().github_data.ros_repo_22,
MongoClient().github_data.ros_repo_23,
MongoClient().github_data.ros_repo_24,
MongoClient().github_data.ros_repo_25,
MongoClient().github_data.ros_repo_26,
MongoClient().github_data.ros_repo_27,
MongoClient().github_data.ros_repo_28,
MongoClient().github_data.ros_repo_29,
MongoClient().github_data.ros_repo_30,
MongoClient().github_data.ros_repo_31,
MongoClient().github_data.ros_repo_32,
MongoClient().github_data.ros_repo_33,
MongoClient().github_data.ros_repo_34,
MongoClient().github_data.ros_repo_35,
MongoClient().github_data.ros_repo_36,
MongoClient().github_data.ros_repo_37,
MongoClient().github_data.ros_repo_38,
MongoClient().github_data.ros_repo_39,
MongoClient().github_data.ros_repo_40,
MongoClient().github_data.ros_repo_41,
MongoClient().github_data.ros_repo_42,
MongoClient().github_data.ros_repo_43,
MongoClient().github_data.ros_repo_44,
MongoClient().github_data.ros_repo_45,
MongoClient().github_data.ros_repo_46,
MongoClient().github_data.ros_repo_47,
MongoClient().github_data.ros_repo_48,
MongoClient().github_data.ros_repo_49,
MongoClient().github_data.ros_repo_50,
MongoClient().github_data.ros_repo_51,
MongoClient().github_data.ros_repo_52,
MongoClient().github_data.ros_repo_53,
MongoClient().github_data.ros_repo_54,
MongoClient().github_data.ros_repo_55,
MongoClient().github_data.ros_repo_56,
MongoClient().github_data.ros_repo_57,
MongoClient().github_data.ros_repo_58,
MongoClient().github_data.ros_repo_59,
MongoClient().github_data.ros_repo_60,
MongoClient().github_data.ros_repo_61,
MongoClient().github_data.ros_repo_62,
MongoClient().github_data.ros_repo_63,
MongoClient().github_data.ros_repo_64,
MongoClient().github_data.ros_repo_65,
MongoClient().github_data.ros_repo_66,
MongoClient().github_data.ros_repo_67,
MongoClient().github_data.ros_repo_68,
MongoClient().github_data.ros_repo_69,
MongoClient().github_data.ros_repo_70,
MongoClient().github_data.ros_repo_71,
MongoClient().github_data.ros_repo_72,
MongoClient().github_data.ros_repo_73,
MongoClient().github_data.ros_repo_74,
MongoClient().github_data.ros_repo_75,
MongoClient().github_data.ros_repo_76,
MongoClient().github_data.ros_repo_77,
MongoClient().github_data.ros_repo_78,
MongoClient().github_data.ros_repo_79,
MongoClient().github_data.ros_repo_80,
MongoClient().github_data.ros_repo_81,
MongoClient().github_data.ros_repo_82,
MongoClient().github_data.ros_repo_83,
MongoClient().github_data.ros_repo_84,
MongoClient().github_data.ros_repo_85,
MongoClient().github_data.ros_repo_86,
MongoClient().github_data.ros_repo_87,
MongoClient().github_data.ros_repo_88,
MongoClient().github_data.ros_repo_89,
MongoClient().github_data.ros_repo_90,
MongoClient().github_data.ros_repo_91,
MongoClient().github_data.ros_repo_92,
MongoClient().github_data.ros_repo_93,
MongoClient().github_data.ros_repo_94,
MongoClient().github_data.ros_repo_95,
MongoClient().github_data.ros_repo_96,
MongoClient().github_data.ros_repo_97,
MongoClient().github_data.ros_repo_98,
MongoClient().github_data.ros_repo_99,
MongoClient().github_data.ros_repo_100,
MongoClient().github_data.ros_repo_101,
MongoClient().github_data.ros_repo_102,
MongoClient().github_data.ros_repo_103,
MongoClient().github_data.ros_repo_104,
MongoClient().github_data.ros_repo_105,
MongoClient().github_data.ros_repo_106,
MongoClient().github_data.ros_repo_107,
MongoClient().github_data.ros_repo_108,
MongoClient().github_data.ros_repo_109,
MongoClient().github_data.ros_repo_110,
MongoClient().github_data.ros_repo_111,
MongoClient().github_data.ros_repo_112,
MongoClient().github_data.ros_repo_113,
MongoClient().github_data.ros_repo_114,
MongoClient().github_data.ros_repo_115,
MongoClient().github_data.ros_repo_116,
MongoClient().github_data.ros_repo_117,
MongoClient().github_data.ros_repo_118,
MongoClient().github_data.ros_repo_119,
MongoClient().github_data.ros_repo_120,
MongoClient().github_data.ros_repo_121,
MongoClient().github_data.ros_repo_122,
MongoClient().github_data.ros_repo_123,
MongoClient().github_data.ros_repo_124,
MongoClient().github_data.ros_repo_125,
MongoClient().github_data.ros_repo_126,
MongoClient().github_data.ros_repo_127,
MongoClient().github_data.ros_repo_128,
MongoClient().github_data.ros_repo_129,
MongoClient().github_data.ros_repo_130,
MongoClient().github_data.ros_repo_131,
MongoClient().github_data.ros_repo_132,
MongoClient().github_data.ros_repo_133,
MongoClient().github_data.ros_repo_134,
MongoClient().github_data.ros_repo_135,
MongoClient().github_data.ros_repo_136,
MongoClient().github_data.ros_repo_137,
MongoClient().github_data.ros_repo_138,
MongoClient().github_data.ros_repo_139,
MongoClient().github_data.ros_repo_140,
MongoClient().github_data.ros_repo_141,
MongoClient().github_data.ros_repo_142,
MongoClient().github_data.ros_repo_143,
MongoClient().github_data.ros_repo_144,
MongoClient().github_data.ros_repo_145,
MongoClient().github_data.ros_repo_146,
MongoClient().github_data.ros_repo_147,
MongoClient().github_data.ros_repo_148,
MongoClient().github_data.ros_repo_149,
MongoClient().github_data.ros_repo_150,
MongoClient().github_data.ros_repo_151,
MongoClient().github_data.ros_repo_152,
MongoClient().github_data.ros_repo_153,
MongoClient().github_data.ros_repo_154,
MongoClient().github_data.ros_repo_155,
MongoClient().github_data.ros_repo_156,
MongoClient().github_data.ros_repo_157,
MongoClient().github_data.ros_repo_158,
MongoClient().github_data.ros_repo_159,
MongoClient().github_data.ros_repo_160,
MongoClient().github_data.ros_repo_161,
MongoClient().github_data.ros_repo_162,
MongoClient().github_data.ros_repo_163,
MongoClient().github_data.ros_repo_164,
MongoClient().github_data.ros_repo_165,
MongoClient().github_data.ros_repo_166,
MongoClient().github_data.ros_repo_167,
MongoClient().github_data.ros_repo_168,
MongoClient().github_data.ros_repo_169,
MongoClient().github_data.ros_repo_170,
MongoClient().github_data.ros_repo_171,
MongoClient().github_data.ros_repo_172,
MongoClient().github_data.ros_repo_173,
MongoClient().github_data.ros_repo_174,
MongoClient().github_data.ros_repo_175,
MongoClient().github_data.ros_repo_176,
MongoClient().github_data.ros_repo_177,
MongoClient().github_data.ros_repo_178,
MongoClient().github_data.ros_repo_179,
MongoClient().github_data.ros_repo_180,
MongoClient().github_data.ros_repo_181,
MongoClient().github_data.ros_repo_182,
MongoClient().github_data.ros_repo_183,
MongoClient().github_data.ros_repo_184,
MongoClient().github_data.ros_repo_185,
MongoClient().github_data.ros_repo_186,
MongoClient().github_data.ros_repo_187,
MongoClient().github_data.ros_repo_188,
MongoClient().github_data.ros_repo_189,
MongoClient().github_data.ros_repo_190,
MongoClient().github_data.ros_repo_191,
MongoClient().github_data.ros_repo_192,
MongoClient().github_data.ros_repo_193,
MongoClient().github_data.ros_repo_194,
MongoClient().github_data.ros_repo_195,
MongoClient().github_data.ros_repo_196,
MongoClient().github_data.ros_repo_197,
MongoClient().github_data.ros_repo_198,
MongoClient().github_data.ros_repo_199,
MongoClient().github_data.ros_repo_200,
MongoClient().github_data.ros_repo_201,
MongoClient().github_data.ros_repo_202,
MongoClient().github_data.ros_repo_203,
MongoClient().github_data.ros_repo_204,
MongoClient().github_data.ros_repo_205,
MongoClient().github_data.ros_repo_206,
MongoClient().github_data.ros_repo_207,
MongoClient().github_data.ros_repo_208,
MongoClient().github_data.ros_repo_209,
MongoClient().github_data.ros_repo_210,
MongoClient().github_data.ros_repo_211,
MongoClient().github_data.ros_repo_212,
MongoClient().github_data.ros_repo_213,
MongoClient().github_data.ros_repo_214,
MongoClient().github_data.ros_repo_215,
MongoClient().github_data.ros_repo_216,
MongoClient().github_data.ros_repo_217,
MongoClient().github_data.ros_repo_218,
MongoClient().github_data.ros_repo_219,
MongoClient().github_data.ros_repo_220,
MongoClient().github_data.ros_repo_221,
MongoClient().github_data.ros_repo_222,
MongoClient().github_data.ros_repo_223,
MongoClient().github_data.ros_repo_224,
MongoClient().github_data.ros_repo_225,
MongoClient().github_data.ros_repo_226,
MongoClient().github_data.ros_repo_227,
MongoClient().github_data.ros_repo_228,
MongoClient().github_data.ros_repo_229,
MongoClient().github_data.ros_repo_230,
MongoClient().github_data.ros_repo_231,
MongoClient().github_data.ros_repo_232,
MongoClient().github_data.ros_repo_233,
MongoClient().github_data.ros_repo_234,
MongoClient().github_data.ros_repo_235,
MongoClient().github_data.ros_repo_236,
MongoClient().github_data.ros_repo_237,
MongoClient().github_data.ros_repo_238,
MongoClient().github_data.ros_repo_239,
MongoClient().github_data.ros_repo_240,
MongoClient().github_data.ros_repo_241,
MongoClient().github_data.ros_repo_242,
MongoClient().github_data.ros_repo_243,
MongoClient().github_data.ros_repo_244,
MongoClient().github_data.ros_repo_245,
MongoClient().github_data.ros_repo_246,
MongoClient().github_data.ros_repo_247,
MongoClient().github_data.ros_repo_248,
MongoClient().github_data.ros_repo_249,
MongoClient().github_data.ros_repo_250]

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

    first = numpy.percentile(myList, 25)
    third = numpy.percentile(myList, 75)

    below_outliers = len([i for i in myList if i < first])
    boxplot = len([i for i in myList if third > i > first])
    above_outliers = len([i for i in myList if i > third])
    below_outliers_prc = below_outliers / len_list
    boxplot_prc = boxplot / len_list
    above_outliers_prc = above_outliers / len_list
    # print below_outliers_prc
    # print boxplot_prc
    # print above_outliers_prc

    return {
        'dense': below_outliers,
        'normal': boxplot,
        'dispersed': above_outliers,
        'dense_prc': below_outliers_prc,
        'normal_prc': boxplot_prc,
        'dispersed_prc': above_outliers_prc
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

                    if len(entry) > 0:
                        sorted_entry = sorted(entry, key=lambda l: l['created_at'])
                        process_issues_dates(sorted_entry, e.get('name'))
                        process_commits_between_issues(sorted_entry, e.get('name'))
                        print 'repo ('+str(k) + ') is done.'
                        results.save("dist_ros_1_250.xls")
                else:
                    print str(k) + ' is not a complete processed repository'

        except Exception as er:
            print '-----'*10
            print er.message
            print '-----'*10
