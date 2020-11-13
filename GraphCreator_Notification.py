import pprint

import networkx as nx
from datetime import datetime
from datetime import timedelta
from pymongo import MongoClient
import numpy
import random
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


def run_simulator(prob):

    first_months_assessment = 3
    issue_opening_acceptance_prob = prob
    repeat_notification = 86400
    hr = [1, 3, 6, 12, 24]

    for i in range(0, len(db_list)):
        issue_regularity_simulator(db_list[i], first_months_assessment,issue_opening_acceptance_prob, repeat_notification, hr)
        print 'repo ('+str(prob)+' --> '+str(i)+') has completed'

    print '*' * 200


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


def issue_regularity_simulator(first_months_list, len_total, prob):

    repeat = 86400
    try:
        if len_total > 5:
            dist = distribution(first_months_list)
            mean = dist['mean']
            std = dist['std']

            for i in range(0, len_total):
                ww = dist['dispersed_prc']+0.01
                weight = [1-ww, dist['dispersed_prc'], 0.01]
                nx = next_time_range(first_months_list, mean, std, weight)
                start = nx['start']
                end = nx['end']
                rn = random_num(start, end)

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

            return first_months_list

    except Exception as er:
        print er.message
        return []


def issues_in_range(myList, hr):

    issues = []
    for k in range(0, len(hr)):
        start = numpy.mean(myList) - (hr[k] * 3600)
        end = numpy.mean(myList) + (hr[k] * 3600)
        count_issues = len([i for i in myList if start < i < end])
        issues.append(count_issues)

    return issues


def issues_time_window(db, month, hr):
    try:
        count = db.count()
        if count > 0:
            main_entry = db.find()[count - 1]
            if main_entry.get('contributors_count'):
                entry = []
                j = 0
                for e in db.find():
                    j += 1
                    if not e.get('contributors_count'):
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
                    'repo_name' : main_entry.get('name'),
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

    # weights = [0.85, 0.13, 0.02]
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


def before_notification_graph_generator():

    hr = [1, 3, 6, 12, 24]

    issue_range = \
        [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50,
         0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00]

    first_days_pattern = \
        [3, 7, 14, 21, 30, 60, 90, 120, 150, 180, 210,
         240, 270, 300, 330, 360, 450, 540, 630, 720, 1000]

    issue_related_repos = [[], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], []]
    first_days_pattern_related_repos = \
        [[], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], []]

    current_lang = []
    lang_ind = 0
    lang_log = []

    for i in range(0, len(db_list)):
        db = db_list[i]
        try:
            count = db.count()
            if count > 0:
                main_entry = db.find()[count - 1]
                day_repo_created = main_entry['created_at']
                lang = main_entry['language']
                if main_entry.get('contributors_count'):
                    entry = []
                    j = 0
                    for e in db.find():
                        j += 1
                        if not e.get('contributors_count'):
                            if e.get('type') == 'IssueOpened':
                                entry.append(e.get('created_at'))

                    sorted_entry = sorted(entry)
                    len_sorted = len(sorted_entry)
                    days_before_first_issue = Utility.time_diff_day(day_repo_created, sorted_entry[0])

                    all_months_days_between_issues = []
                    for dt in range(0, len_sorted - 1):
                        all_months_days_between_issues.append(Utility.time_diff(sorted_entry[dt], sorted_entry[dt + 1]))

                    dist = distribution(all_months_days_between_issues)
                    issues_count_in_range = issues_in_range(all_months_days_between_issues, hr)
                    issues_around_mean_3hr = issues_count_in_range[1]
                    repo_name = main_entry.get('name')
                    issues_count = dist['issue_count']

                    # Find to which group of repos this repo belongs
                    if issues_count > 0:
                        issue_prc = issues_around_mean_3hr / float(issues_count)

                        # this will be based on the "percentage of the issues distances" pattern
                        j2 = [i for i in issue_range if i >= issue_prc]
                        index = len(issue_range) - len(j2)
                        issue_related_repos[index].append(repo_name)

                        graph.add_node(repo_name, name=repo_name, lang=lang, group=index)

                        # this will be based on the "days to open the first issue" pattern
                        if days_before_first_issue > 720:
                            j2 = [1000]
                        else:
                            j2 = [i for i in first_days_pattern if i >= days_before_first_issue]

                        index = len(first_days_pattern) - len(j2)
                        first_days_pattern_related_repos[index].append(repo_name)

                        if lang not in lang_log:
                            current_lang.append({
                                'lang': lang,
                                'index': lang_ind
                            })
                            lang_log.append(lang)
                            lang_ind += 1
                    print 'this repo is done -> ' + repo_name

                else:
                    print ' is not a complete processed repository'

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
    for entry in issue_related_repos:
        for i in range(0, len(entry)):
            for j in range(i+1, len(entry)):
                node1 = entry[i]
                node2 = entry[j]
                if node1 != node2:
                    graph.add_edge(node1, node2, weight=1)

    # edges between "first day pattern" related repos
    for entry in first_days_pattern_related_repos:
        for i in range(0, len(entry)):
            for j in range(0, len(entry)):
                node1 = entry[i]
                node2 = entry[j]
                if graph.has_edge(node1, node2):
                    graph[node1][node2]['weight'] = 2
                elif node1 != node2:
                    graph.add_edge(node1, node2, weight=1)

    # edges between language related repos
    # for entry in l:
    #     for i in range(0, len(entry)):
    #         for j in range(0, len(entry)):
    #             node1 = entry[i]
    #             node2 = entry[j]
    #
    #             if graph.has_edge(node1, node2):
    #                 graph[node1][node2]['weight'] = 2
    #             elif node1 != node2:
    #                 graph.add_edge(node1, node2, weight=1)

    nx.write_graphml(graph, "/Users/Abduljaleel/Desktop/issues_firstPattern.graphml")


def after_notification_graph_generator(prob):

    month = 3
    hr = [1, 3, 6, 12, 24]

    issue_range = \
        [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50,
         0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00]

    first_days_pattern = \
        [3, 7, 14, 21, 30, 60, 90, 120, 150, 180, 210,
         240, 270, 300, 330, 360, 450, 540, 630, 720, 1000]

    issue_related_repos = [[], [], [], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], [], []]
    first_days_pattern_related_repos = \
        [[], [], [], [], [], [], [], [], [], [],
         [], [], [], [], [], [], [], [], [], [], []]

    current_lang = []
    lang_ind = 0
    lang_log = []

    for i in range(0, len(db_list)):
        db = db_list[i]
        try:
            count = db.count()
            if count > 0:
                main_entry = db.find()[count - 1]
                day_repo_created = main_entry['created_at']
                lang = main_entry['language']
                if main_entry.get('contributors_count'):

                    entry = []
                    j = 0
                    for e in db.find():
                        j += 1
                        if not e.get('contributors_count'):
                            if e.get('type') == 'IssueOpened':
                                entry.append(e.get('created_at'))

                    sorted_entry = sorted(entry)
                    len_sorted = len(sorted_entry)

                    first_day = datetime.strptime(sorted_entry[0], '%Y-%m-%dT%H:%M:%SZ')
                    end_date = first_day + timedelta(days=month*30)

                    days_before_first_issue = Utility.time_diff_day(day_repo_created, sorted_entry[0])

                    first_months_issues = []
                    for i in range (0, len_sorted):
                        if datetime.strptime(sorted_entry[i], '%Y-%m-%dT%H:%M:%SZ') < end_date:
                            first_months_issues.append(sorted_entry[i])

                    first_months_days_between_issues = []
                    for dt in range(0, len(first_months_issues) - 1):
                        first_months_days_between_issues.append(Utility.time_diff(first_months_issues[dt], first_months_issues[dt + 1]))

                    all_months_days_between_issues = []
                    for dt in range(0, len_sorted - 1):
                        all_months_days_between_issues.append(Utility.time_diff(sorted_entry[dt], sorted_entry[dt + 1]))

                    first_month_list = first_months_days_between_issues
                    len_total = len(all_months_days_between_issues) - len(first_months_days_between_issues)

                    # the simulator
                    final_list_after_simulator = issue_regularity_simulator(first_month_list, len_total, prob)

                    dist = distribution(final_list_after_simulator)
                    issues_count_in_range = issues_in_range(final_list_after_simulator, hr)
                    issues_around_mean_3hr = issues_count_in_range[1]
                    repo_name = main_entry.get('name')
                    issues_count = dist['issue_count']

                    # Find to which group of repos this repo belongs
                    if issues_count > 0:
                        issue_prc = issues_around_mean_3hr / float(issues_count)

                        # this will be based on the "percentage of the issues distances" pattern
                        j2 = [i for i in issue_range if i >= issue_prc]
                        index = len(issue_range) - len(j2)
                        issue_related_repos[index].append(repo_name)

                        graph.add_node(repo_name, name=repo_name, lang=lang, group=index)

                        # this will be based on the "days to open the first issue" pattern
                        if days_before_first_issue > 720:
                            j2 = [1000]
                        else:
                            j2 = [i for i in first_days_pattern if i >= days_before_first_issue]

                        index = len(first_days_pattern) - len(j2)
                        first_days_pattern_related_repos[index].append(repo_name)

                        if lang not in lang_log:
                            current_lang.append({
                                'lang': lang,
                                'index': lang_ind
                            })
                            lang_log.append(lang)
                            lang_ind += 1
                    print 'this repo is done -> ' + repo_name
                else:
                    print ' is not a complete processed repository'

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
    for entry in issue_related_repos:
        for i in range(0, len(entry)):
            for j in range(i+1, len(entry)):
                node1 = entry[i]
                node2 = entry[j]
                if node1 != node2:
                    graph.add_edge(node1, node2, weight=1)

    # edges between "first day pattern" related repos
    # for entry in first_days_pattern_related_repos:
    #     for i in range(0, len(entry)):
    #         for j in range(0, len(entry)):
    #             node1 = entry[i]
    #             node2 = entry[j]
    #             if graph.has_edge(node1, node2):
    #                 graph[node1][node2]['weight'] = 2
    #             elif node1 != node2:
    #                 graph.add_edge(node1, node2, weight=1)

    # edges between language related repos
    for entry in l:
        for i in range(0, len(entry)):
            for j in range(0, len(entry)):
                node1 = entry[i]
                node2 = entry[j]

                if graph.has_edge(node1, node2):
                    graph[node1][node2]['weight'] = 2
                elif node1 != node2:
                    graph.add_edge(node1, node2, weight=1)

    nx.write_graphml(graph, "/Users/Abduljaleel/Desktop/IssuesPattern_Lang"+str(prob)+".graphml")


if __name__ == "__main__":
    graph = nx.Graph()
    # before_notification_graph_generator()
    after_notification_graph_generator(0.9)
    # after_notification_graph_generator(0.6)
    # after_notification_graph_generator(0.9)
