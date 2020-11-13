from datetime import datetime
from datetime import timedelta

import xlwt
from pymongo import MongoClient
import numpy
import random
import matplotlib.pyplot as plt

import Utility

__author__ = 'Abduljaleel Al Rubaye'

final_time_line_db = MongoClient().github_data.final_time_line

Issue_Sheet_first_row = [
    'repo_name',
    'issues_count',
    'old_mean',
    'old_std',
    'old_dense_issues',
    'old_normal_issues',
    'old_dispersed_issues',
    'old_dense_issues_prc',
    'old_normal_issues_prc',
    'old_dispersed_issues_prc',
    'old_range',
    'old_issues_dens_in_mean_std_range',
    'old_issues_around_mean_1hr',
    'old_issues_around_mean_3hr',
    'old_issues_around_mean_6hr',
    'old_issues_around_mean_12hr',
    'old_issues_around_mean_24hr',
    'new_mean',
    'new_std',
    'new_dense_issues',
    'new_normal_issues',
    'new_dispersed_issues',
    'new_dense_issues_prc',
    'new_normal_issues_prc',
    'new_dispersed_issues_prc',
    'new_range',
    'new_issues_dens_in_mean_std_range',
    'new_issues_around_mean_1hr',
    'new_issues_around_mean_3hr',
    'new_issues_around_mean_6hr',
    'new_issues_around_mean_12hr',
    'new_issues_around_mean_24hr'
]


def histogram(li):
    plt.hist(li, bins=6)
    plt.show()


def issues_in_range(myList, hr):

    issues = []
    for k in range (0, len(hr)):
        start = numpy.mean(myList) - (hr[k] * 3600)
        end = numpy.mean(myList) + (hr[k] * 3600)
        count_issues = len([i for i in myList if start < i < end])
        issues.append(count_issues)

    return issues


def distribution(myList):
    len_list = float(len(myList))
    mean = numpy.mean(myList)
    median = numpy.median(myList)
    std = numpy.std(myList)
    std_minus_one = mean - std
    std_plus_one = mean + std
    count_minus = len([i for i in myList if i < std_minus_one])
    count_mid = len([i for i in myList if std_minus_one < i < std_plus_one])
    count_plus = len([i for i in myList if i > std_plus_one])
    perc_minus = 0 if len_list == 0 else count_minus / float(len_list)
    perc_mid = 0 if len_list == 0 else count_mid / float(len_list)
    perc_plus = 0 if len_list == 0 else count_plus / float(len_list)

    return {
        'mean': mean,
        'median': median,
        'std': std,
        'issue_count': len(myList),
        'dense': count_minus,
        'normal': count_mid,
        'dispersed': count_plus,
        'dense_prc': perc_minus,
        'normal_prc': perc_mid,
        'dispersed_prc': perc_plus
    }


def random_num(start, num):
    return random.randint(start, num)


def issue_regularity_simulator(db, name, month, prob, repeat, hr):

    try:
        issues_list = issues_time_window(db, name, month, hr)
        first_months_list = issues_list['initial_list_on_the_first_months']
        len_total = issues_list['final_list_length']

        if len > 5:
            dist = distribution(first_months_list)
            mean = dist['mean']
            std = dist['std']

            for i in range(0, len_total):
                ww = dist['dispersed_prc']+0.01
                weight = [1-ww, dist['dispersed_prc'],0.01]
                nx = next_time_range(first_months_list, mean, std, weight)
                start = nx['start']
                end = nx['end']
                rn = random_num(start, end)
                # print 'first rn = '+str(rn)

                if rn > mean:

                    accept_issue_notification = numpy.random.choice([True, False], 1, p=[prob, 1-prob])[0]

                    if accept_issue_notification:
                        rn = int(mean)
                    else:
                        cron = mean+repeat
                        while rn > cron:
                            accept_issue_notification = numpy.random.choice([True, False], 1, p=[prob, 1-prob])[0]
                            if accept_issue_notification:
                                rn = int(cron)
                                break
                            cron += repeat

                first_months_list.append(rn)

                dist = distribution(first_months_list)
                mean = dist['mean']
                std = dist['std']

            rangee = (dist['mean']+dist['std'])-(dist['mean']-dist['std'])
            issues_count_in_range = issues_in_range(first_months_list, hr)
            # print 'Final list statistics'
            # print 'mean = ' + str(dist['mean'])
            # print 'median = '+ str(dist['median'])
            # print 'std = ' + str(dist['std'])
            # print 'max = ' + str(max(first_months_list))
            # print 'dense_prc = ' + str(dist['dense_prc'])
            # print 'normal_prc = ' + str(dist['normal_prc'])
            # print 'dispersed_prc = ' + str(dist['dispersed_prc'])
            # print '......... Issue Density per seconds on the range [mean-std, mean+std]=' + str(dist['normal'] / float(rangee))
            # print '......... # Issues in range [mean-6hrs, mean+6hrs] = ' + str(issues_count_in_range)

            list_to_sheet = {
                'repo_name': issues_list['repo_name'],
                'issues_count': issues_list['issues_count'],
                'old_mean': issues_list['old_mean'],
                'old_std': issues_list['old_std'],
                'old_dense_issues': issues_list['old_dense_issues'],
                'old_normal_issues': issues_list['old_normal_issues'],
                'old_dispersed_issues': issues_list['old_dispersed_issues'],
                'old_dense_issues_prc': issues_list['old_dense_issues_prc'],
                'old_normal_issues_prc': issues_list['old_normal_issues_prc'],
                'old_dispersed_issues_prc': issues_list['old_dispersed_issues_prc'],
                'old_range': issues_list['old_range'],
                'old_issues_dens_in_mean_std_range': issues_list['old_issues_dens_in_mean_std_range'],
                'old_issues_around_mean_1hr': issues_list['old_issues_around_mean_1hr'],
                'old_issues_around_mean_3hr': issues_list['old_issues_around_mean_3hr'],
                'old_issues_around_mean_6hr': issues_list['old_issues_around_mean_6hr'],
                'old_issues_around_mean_12hr': issues_list['old_issues_around_mean_12hr'],
                'old_issues_around_mean_24hr': issues_list['old_issues_around_mean_24hr'],
                'new_mean': dist['mean'],
                'new_std': dist['std'],
                'new_dense_issues': dist['dense'],
                'new_normal_issues': dist['normal'],
                'new_dispersed_issues': dist['dispersed'],
                'new_dense_issues_prc': dist['dense_prc'],
                'new_normal_issues_prc': dist['normal_prc'],
                'new_dispersed_issues_prc': dist['dispersed_prc'],
                'new_range': rangee,
                'new_issues_dens_in_mean_std_range': dist['normal'] / float(rangee),
                'new_issues_around_mean_1hr': issues_count_in_range[0],
                'new_issues_around_mean_3hr': issues_count_in_range[1],
                'new_issues_around_mean_6hr': issues_count_in_range[2],
                'new_issues_around_mean_12hr': issues_count_in_range[3],
                'new_issues_around_mean_24hr': issues_count_in_range[4]
            }

            export_to_sheet(list_to_sheet)
    except Exception as er:
        print er.message


def issues_time_window(db, name, month, hr):
    try:
        count = len(db)
        if count > 0:
            entry = []
            for e in db:
                if e.get('type') == 'IssueOpened':
                    entry.append(e.get('created_at'))

            sorted_entry = sorted(entry)

            len_sorted = len(sorted_entry)
            first_day = datetime.strptime(sorted_entry[0], '%Y-%m-%dT%H:%M:%SZ')
            end_date = first_day + timedelta(days=month*30)

            first_months_issues = []
            all_months_issues = []

            for i in range (0, len_sorted):
                if datetime.strptime(sorted_entry[i], '%Y-%m-%dT%H:%M:%SZ') < end_date:
                    first_months_issues.append(sorted_entry[i])
                    all_months_issues.append(sorted_entry[i])
                else:
                    all_months_issues.append(sorted_entry[i])

            first_months_days_between_issues = []
            for dt in range(0, len(first_months_issues) - 1):
                first_months_days_between_issues.append(Utility.time_diff(first_months_issues[dt], first_months_issues[dt + 1]))

            all_months_days_between_issues = []
            for dt in range(0, len(all_months_issues) - 1):
                all_months_days_between_issues.append(Utility.time_diff(all_months_issues[dt], all_months_issues[dt + 1]))

            dist = distribution(all_months_days_between_issues)
            rangee = (dist['mean']+dist['std'])-(dist['mean']-dist['std'])
            issues_count_in_range = issues_in_range(all_months_days_between_issues, hr)

            return {
                'initial_list_on_the_first_months': first_months_days_between_issues,
                'final_list_length': len(all_months_days_between_issues) - len(first_months_days_between_issues),
                'repo_name' : name,
                'issues_count': dist['issue_count'],
                'old_mean': dist['mean'],
                'old_std': dist['std'],
                'old_dense_issues': dist['dense'],
                'old_normal_issues': dist['normal'],
                'old_dispersed_issues': dist['dispersed'],
                'old_dense_issues_prc': dist['dense_prc'],
                'old_normal_issues_prc': dist['normal_prc'],
                'old_dispersed_issues_prc': dist['dispersed_prc'],
                'old_range': rangee,
                'old_issues_dens_in_mean_std_range': dist['normal'] / float(rangee),
                'old_issues_around_mean_1hr': issues_count_in_range[0],
                'old_issues_around_mean_3hr': issues_count_in_range[1],
                'old_issues_around_mean_6hr': issues_count_in_range[2],
                'old_issues_around_mean_12hr': issues_count_in_range[3],
                'old_issues_around_mean_24hr': issues_count_in_range[4]
            }

        else:
            print ' is not a complete processed repository'

    except Exception as er:
        print er.message


def next_time_range(myList, mean, std, weight):

    parts = [1, 2, 3]

    y = numpy.random.choice(parts, 1, p=weight)[0]

    if y == 1:
        start = 0
        end = int(mean+std)
        # print 'random between 0 and mean+std'
    elif y == 2:
        start = int(mean+std)
        end = max(myList)
        # print 'random between mean+std and max'
    else:
        start = max(myList)
        end = max(myList)+int(std)
        # print 'random between max and max+std'

    return {
        'start': start,
        'end': end
    }


def define_xls(num, prob):
    global results, excel_file, sheet1, row_issue
    row_issue = 0
    excel_file = "REG_issue_"+str(prob)+"_regularity"+str(num)+".xls"
    results = xlwt.Workbook(encoding="utf-8")
    sheet1 = results.add_sheet('Issues')

    col = 0
    for i in range(0, len(Issue_Sheet_first_row)):
        sheet1.write(row_issue , col, str(Issue_Sheet_first_row[i]))
        col += 1


def export_to_sheet(myList):
    global results, excel_file, sheet1, row_issue
    row_issue += 1
    col = 0
    for i in range (0, len(myList)):
        sheet1.write(row_issue, col, str(myList[Issue_Sheet_first_row[i]]))
        col += 1
    results.save(excel_file)


def run_simulator(num, prob):
    global results, excel_file, sheet1, row_issue

    define_xls(num, prob)

    first_months_assessment = 3
    issue_opening_acceptance_prob = prob
    repeat_notification = 86400
    hr = [1,3,6,12,24]

    k = 0
    for e in final_time_line_db.find():
        try:
            if e.get('time_line'):
                issue_regularity_simulator(e.get('time_line'), e.get('name'), first_months_assessment,issue_opening_acceptance_prob, repeat_notification, hr)
                print 'repo ('+str(prob)+' --> '+str(k)+') has completed'
        except Exception as er:
            print er
        k += 1

    print '*' * 200


if __name__ == "__main__":

    num = ''
    # run_simulator(num, 0.3)
    run_simulator(num, 0.6)
    run_simulator(num, 0.9)




