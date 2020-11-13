from datetime import datetime
from datetime import timedelta

import xlwt
from pymongo import MongoClient
import numpy
import random
import matplotlib.pyplot as plt

import Utility

__author__ = 'Abduljaleel Al Rubaye'

global num


num = '_330_660_'
db_list = [
MongoClient().github_data.ros_repo_331,
MongoClient().github_data.ros_repo_332,
MongoClient().github_data.ros_repo_333,
MongoClient().github_data.ros_repo_334,
MongoClient().github_data.ros_repo_335,
MongoClient().github_data.ros_repo_336,
MongoClient().github_data.ros_repo_337,
MongoClient().github_data.ros_repo_338,
MongoClient().github_data.ros_repo_339,
MongoClient().github_data.ros_repo_340,
MongoClient().github_data.ros_repo_341,
MongoClient().github_data.ros_repo_342,
MongoClient().github_data.ros_repo_343,
MongoClient().github_data.ros_repo_344,
MongoClient().github_data.ros_repo_345,
MongoClient().github_data.ros_repo_346,
MongoClient().github_data.ros_repo_347,
MongoClient().github_data.ros_repo_348,
MongoClient().github_data.ros_repo_349,
MongoClient().github_data.ros_repo_350,
MongoClient().github_data.ros_repo_351,
MongoClient().github_data.ros_repo_352,
MongoClient().github_data.ros_repo_353,
MongoClient().github_data.ros_repo_354,
MongoClient().github_data.ros_repo_355,
MongoClient().github_data.ros_repo_356,
MongoClient().github_data.ros_repo_357,
MongoClient().github_data.ros_repo_358,
MongoClient().github_data.ros_repo_359,
MongoClient().github_data.ros_repo_360,
MongoClient().github_data.ros_repo_361,
MongoClient().github_data.ros_repo_362,
MongoClient().github_data.ros_repo_363,
MongoClient().github_data.ros_repo_364,
MongoClient().github_data.ros_repo_365,
MongoClient().github_data.ros_repo_366,
MongoClient().github_data.ros_repo_367,
MongoClient().github_data.ros_repo_368,
MongoClient().github_data.ros_repo_369,
MongoClient().github_data.ros_repo_370,
MongoClient().github_data.ros_repo_371,
MongoClient().github_data.ros_repo_372,
MongoClient().github_data.ros_repo_373,
MongoClient().github_data.ros_repo_374,
MongoClient().github_data.ros_repo_375,
MongoClient().github_data.ros_repo_376,
MongoClient().github_data.ros_repo_377,
MongoClient().github_data.ros_repo_378,
MongoClient().github_data.ros_repo_379,
MongoClient().github_data.ros_repo_380,
MongoClient().github_data.ros_repo_381,
MongoClient().github_data.ros_repo_382,
MongoClient().github_data.ros_repo_383,
MongoClient().github_data.ros_repo_384,
MongoClient().github_data.ros_repo_385,
MongoClient().github_data.ros_repo_386,
MongoClient().github_data.ros_repo_387,
MongoClient().github_data.ros_repo_388,
MongoClient().github_data.ros_repo_389,
MongoClient().github_data.ros_repo_390,
MongoClient().github_data.ros_repo_391,
MongoClient().github_data.ros_repo_392,
MongoClient().github_data.ros_repo_393,
MongoClient().github_data.ros_repo_394,
MongoClient().github_data.ros_repo_395,
MongoClient().github_data.ros_repo_396,
MongoClient().github_data.ros_repo_397,
MongoClient().github_data.ros_repo_398,
MongoClient().github_data.ros_repo_399,
MongoClient().github_data.ros_repo_400,
MongoClient().github_data.ros_repo_401,
MongoClient().github_data.ros_repo_402,
MongoClient().github_data.ros_repo_403,
MongoClient().github_data.ros_repo_404,
MongoClient().github_data.ros_repo_405,
MongoClient().github_data.ros_repo_406,
MongoClient().github_data.ros_repo_407,
MongoClient().github_data.ros_repo_408,
MongoClient().github_data.ros_repo_409,
MongoClient().github_data.ros_repo_410,
MongoClient().github_data.ros_repo_411,
MongoClient().github_data.ros_repo_412,
MongoClient().github_data.ros_repo_413,
MongoClient().github_data.ros_repo_414,
MongoClient().github_data.ros_repo_415,
MongoClient().github_data.ros_repo_416,
MongoClient().github_data.ros_repo_417,
MongoClient().github_data.ros_repo_418,
MongoClient().github_data.ros_repo_419,
MongoClient().github_data.ros_repo_420,
MongoClient().github_data.ros_repo_421,
MongoClient().github_data.ros_repo_422,
MongoClient().github_data.ros_repo_423,
MongoClient().github_data.ros_repo_424,
MongoClient().github_data.ros_repo_425,
MongoClient().github_data.ros_repo_426,
MongoClient().github_data.ros_repo_427,
MongoClient().github_data.ros_repo_428,
MongoClient().github_data.ros_repo_429,
MongoClient().github_data.ros_repo_430,
MongoClient().github_data.ros_repo_431,
MongoClient().github_data.ros_repo_432,
MongoClient().github_data.ros_repo_433,
MongoClient().github_data.ros_repo_434,
MongoClient().github_data.ros_repo_435,
MongoClient().github_data.ros_repo_436,
MongoClient().github_data.ros_repo_437,
MongoClient().github_data.ros_repo_438,
MongoClient().github_data.ros_repo_439,
MongoClient().github_data.ros_repo_440,
MongoClient().github_data.ros_repo_441,
MongoClient().github_data.ros_repo_442,
MongoClient().github_data.ros_repo_443,
MongoClient().github_data.ros_repo_444,
MongoClient().github_data.ros_repo_445,
MongoClient().github_data.ros_repo_446,
MongoClient().github_data.ros_repo_447,
MongoClient().github_data.ros_repo_448,
MongoClient().github_data.ros_repo_449,
MongoClient().github_data.ros_repo_450,
MongoClient().github_data.ros_repo_451,
MongoClient().github_data.ros_repo_452,
MongoClient().github_data.ros_repo_453,
MongoClient().github_data.ros_repo_454,
MongoClient().github_data.ros_repo_455,
MongoClient().github_data.ros_repo_456,
MongoClient().github_data.ros_repo_457,
MongoClient().github_data.ros_repo_458,
MongoClient().github_data.ros_repo_459,
MongoClient().github_data.ros_repo_460,
MongoClient().github_data.ros_repo_461,
MongoClient().github_data.ros_repo_462,
MongoClient().github_data.ros_repo_463,
MongoClient().github_data.ros_repo_464,
MongoClient().github_data.ros_repo_465,
MongoClient().github_data.ros_repo_466,
MongoClient().github_data.ros_repo_467,
MongoClient().github_data.ros_repo_468,
MongoClient().github_data.ros_repo_469,
MongoClient().github_data.ros_repo_470,
MongoClient().github_data.ros_repo_471,
MongoClient().github_data.ros_repo_472,
MongoClient().github_data.ros_repo_473,
MongoClient().github_data.ros_repo_474,
MongoClient().github_data.ros_repo_475,
MongoClient().github_data.ros_repo_476,
MongoClient().github_data.ros_repo_477,
MongoClient().github_data.ros_repo_478,
MongoClient().github_data.ros_repo_479,
MongoClient().github_data.ros_repo_480,
MongoClient().github_data.ros_repo_481,
MongoClient().github_data.ros_repo_482,
MongoClient().github_data.ros_repo_483,
MongoClient().github_data.ros_repo_484,
MongoClient().github_data.ros_repo_485,
MongoClient().github_data.ros_repo_486,
MongoClient().github_data.ros_repo_487,
MongoClient().github_data.ros_repo_488,
MongoClient().github_data.ros_repo_489,
MongoClient().github_data.ros_repo_490,
MongoClient().github_data.ros_repo_491,
MongoClient().github_data.ros_repo_492,
MongoClient().github_data.ros_repo_493,
MongoClient().github_data.ros_repo_494,
MongoClient().github_data.ros_repo_495,
MongoClient().github_data.ros_repo_496,
MongoClient().github_data.ros_repo_497,
MongoClient().github_data.ros_repo_498,
MongoClient().github_data.ros_repo_499,
MongoClient().github_data.ros_repo_500,
MongoClient().github_data.ros_repo_501,
MongoClient().github_data.ros_repo_502,
MongoClient().github_data.ros_repo_503,
MongoClient().github_data.ros_repo_504,
MongoClient().github_data.ros_repo_505,
MongoClient().github_data.ros_repo_506,
MongoClient().github_data.ros_repo_507,
MongoClient().github_data.ros_repo_508,
MongoClient().github_data.ros_repo_509,
MongoClient().github_data.ros_repo_510,
MongoClient().github_data.ros_repo_511,
MongoClient().github_data.ros_repo_512,
MongoClient().github_data.ros_repo_513,
MongoClient().github_data.ros_repo_514,
MongoClient().github_data.ros_repo_515,
MongoClient().github_data.ros_repo_516,
MongoClient().github_data.ros_repo_517,
MongoClient().github_data.ros_repo_518,
MongoClient().github_data.ros_repo_519,
MongoClient().github_data.ros_repo_520,
MongoClient().github_data.ros_repo_521,
MongoClient().github_data.ros_repo_522,
MongoClient().github_data.ros_repo_523,
MongoClient().github_data.ros_repo_524,
MongoClient().github_data.ros_repo_525,
MongoClient().github_data.ros_repo_526,
MongoClient().github_data.ros_repo_527,
MongoClient().github_data.ros_repo_528,
MongoClient().github_data.ros_repo_529,
MongoClient().github_data.ros_repo_530,
MongoClient().github_data.ros_repo_531,
MongoClient().github_data.ros_repo_532,
MongoClient().github_data.ros_repo_533,
MongoClient().github_data.ros_repo_534,
MongoClient().github_data.ros_repo_535,
MongoClient().github_data.ros_repo_536,
MongoClient().github_data.ros_repo_537,
MongoClient().github_data.ros_repo_538,
MongoClient().github_data.ros_repo_539,
MongoClient().github_data.ros_repo_540,
MongoClient().github_data.ros_repo_541,
MongoClient().github_data.ros_repo_542,
MongoClient().github_data.ros_repo_543,
MongoClient().github_data.ros_repo_544,
MongoClient().github_data.ros_repo_545,
MongoClient().github_data.ros_repo_546,
MongoClient().github_data.ros_repo_547,
MongoClient().github_data.ros_repo_548,
MongoClient().github_data.ros_repo_549,
MongoClient().github_data.ros_repo_550,
MongoClient().github_data.ros_repo_551,
MongoClient().github_data.ros_repo_552,
MongoClient().github_data.ros_repo_553,
MongoClient().github_data.ros_repo_554,
MongoClient().github_data.ros_repo_555,
MongoClient().github_data.ros_repo_556,
MongoClient().github_data.ros_repo_557,
MongoClient().github_data.ros_repo_558,
MongoClient().github_data.ros_repo_559,
MongoClient().github_data.ros_repo_560,
MongoClient().github_data.ros_repo_561,
MongoClient().github_data.ros_repo_562,
MongoClient().github_data.ros_repo_563,
MongoClient().github_data.ros_repo_564,
MongoClient().github_data.ros_repo_565,
MongoClient().github_data.ros_repo_566,
MongoClient().github_data.ros_repo_567,
MongoClient().github_data.ros_repo_568,
MongoClient().github_data.ros_repo_569,
MongoClient().github_data.ros_repo_570,
MongoClient().github_data.ros_repo_571,
MongoClient().github_data.ros_repo_572,
MongoClient().github_data.ros_repo_573,
MongoClient().github_data.ros_repo_574,
MongoClient().github_data.ros_repo_575,
MongoClient().github_data.ros_repo_576,
MongoClient().github_data.ros_repo_577,
MongoClient().github_data.ros_repo_578,
MongoClient().github_data.ros_repo_579,
MongoClient().github_data.ros_repo_580,
MongoClient().github_data.ros_repo_581,
MongoClient().github_data.ros_repo_582,
MongoClient().github_data.ros_repo_583,
MongoClient().github_data.ros_repo_584,
MongoClient().github_data.ros_repo_585,
MongoClient().github_data.ros_repo_586,
MongoClient().github_data.ros_repo_587,
MongoClient().github_data.ros_repo_588,
MongoClient().github_data.ros_repo_589,
MongoClient().github_data.ros_repo_590,
MongoClient().github_data.ros_repo_591,
MongoClient().github_data.ros_repo_592,
MongoClient().github_data.ros_repo_593,
MongoClient().github_data.ros_repo_594,
MongoClient().github_data.ros_repo_595,
MongoClient().github_data.ros_repo_596,
MongoClient().github_data.ros_repo_597,
MongoClient().github_data.ros_repo_598,
MongoClient().github_data.ros_repo_599,
MongoClient().github_data.ros_repo_600,
MongoClient().github_data.ros_repo_601,
MongoClient().github_data.ros_repo_602,
MongoClient().github_data.ros_repo_603,
MongoClient().github_data.ros_repo_604,
MongoClient().github_data.ros_repo_605,
MongoClient().github_data.ros_repo_606,
MongoClient().github_data.ros_repo_607,
MongoClient().github_data.ros_repo_608,
MongoClient().github_data.ros_repo_609,
MongoClient().github_data.ros_repo_610,
MongoClient().github_data.ros_repo_611,
MongoClient().github_data.ros_repo_612,
MongoClient().github_data.ros_repo_613,
MongoClient().github_data.ros_repo_614,
MongoClient().github_data.ros_repo_615,
MongoClient().github_data.ros_repo_616,
MongoClient().github_data.ros_repo_617,
MongoClient().github_data.ros_repo_618,
MongoClient().github_data.ros_repo_619,
MongoClient().github_data.ros_repo_620,
MongoClient().github_data.ros_repo_621,
MongoClient().github_data.ros_repo_622,
MongoClient().github_data.ros_repo_623,
MongoClient().github_data.ros_repo_624,
MongoClient().github_data.ros_repo_625,
MongoClient().github_data.ros_repo_626,
MongoClient().github_data.ros_repo_627,
MongoClient().github_data.ros_repo_628,
MongoClient().github_data.ros_repo_629,
MongoClient().github_data.ros_repo_630,
MongoClient().github_data.ros_repo_631,
MongoClient().github_data.ros_repo_632,
MongoClient().github_data.ros_repo_633,
MongoClient().github_data.ros_repo_634,
MongoClient().github_data.ros_repo_635,
MongoClient().github_data.ros_repo_636,
MongoClient().github_data.ros_repo_637,
MongoClient().github_data.ros_repo_638,
MongoClient().github_data.ros_repo_639,
MongoClient().github_data.ros_repo_640,
MongoClient().github_data.ros_repo_641,
MongoClient().github_data.ros_repo_642,
MongoClient().github_data.ros_repo_643,
MongoClient().github_data.ros_repo_644,
MongoClient().github_data.ros_repo_645,
MongoClient().github_data.ros_repo_646,
MongoClient().github_data.ros_repo_647,
MongoClient().github_data.ros_repo_648,
MongoClient().github_data.ros_repo_649,
MongoClient().github_data.ros_repo_650,
MongoClient().github_data.ros_repo_651,
MongoClient().github_data.ros_repo_652,
MongoClient().github_data.ros_repo_653,
MongoClient().github_data.ros_repo_654,
MongoClient().github_data.ros_repo_655,
MongoClient().github_data.ros_repo_656,
MongoClient().github_data.ros_repo_657,
MongoClient().github_data.ros_repo_658,
MongoClient().github_data.ros_repo_659,
MongoClient().github_data.ros_repo_660]



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


def issue_regularity_simulator(db, month, prob, repeat, hr):

    try:
        issues_list = issues_time_window(db, month, hr)
        first_months_list = issues_list['initial_list_on_the_first_months']
        len_total = issues_list['final_list_length']

        if len_total > 5:
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
            if issues_list['issues_count'] > 9:
                export_to_sheet(list_to_sheet)

    except Exception as er:
        print er.message


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

                # print 'First list before simulation'
                # print 'mean = ' + str(dist['mean'])
                # print 'median = '+ str(dist['median'])
                # print 'std = ' + str(dist['std'])
                # print 'max = ' + str(max(all_months_days_between_issues))
                # print 'dense_prc = ' + str(dist['dense_prc'])
                # print 'normal_prc = ' + str(dist['normal_prc'])
                # print 'dispersed_prc = ' + str(dist['dispersed_prc'])
                # print 'range = '+ str(rangee)
                # print '......... Issue Density per seconds on the range [mean-std, mean+std]=' + str(dist['normal'] / float(rangee))
                # print '......... # Issues in the range of [mean - 6hrs, mean+6hrs] = '+str(issues_count_in_range)
                # print '*'*50

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


def define_xls(num, prob):
    global results, excel_file, sheet1, row_issue
    row_issue = 0
    excel_file = "ROS_issue_"+str(prob)+"_regularity"+str(num)+".xls"
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

    for i in range (0, len(db_list)):
        issue_regularity_simulator(db_list[i], first_months_assessment,issue_opening_acceptance_prob, repeat_notification, hr)
        print 'repo ('+str(prob)+' --> '+str(i)+') has completed'

    print '*' * 200


if __name__ == "__main__":

    run_simulator(num, 0.3)
    run_simulator(num, 0.6)
    run_simulator(num, 0.9)




