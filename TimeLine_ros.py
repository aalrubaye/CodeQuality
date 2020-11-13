import pprint
import sys
from datetime import datetime
import xlwt
from textblob import TextBlob
import json
import time
from pymongo import MongoClient
import Utility
import datetime

__author__ = 'Abduljaleel Al Rubaye'

db_list = [
MongoClient().github_data.ros_repo_4301,
MongoClient().github_data.ros_repo_4302,
MongoClient().github_data.ros_repo_4303,
MongoClient().github_data.ros_repo_4304,
MongoClient().github_data.ros_repo_4305,
MongoClient().github_data.ros_repo_4306,
MongoClient().github_data.ros_repo_4307,
MongoClient().github_data.ros_repo_4308,
MongoClient().github_data.ros_repo_4309,
MongoClient().github_data.ros_repo_4310,
MongoClient().github_data.ros_repo_4311,
MongoClient().github_data.ros_repo_4312,
MongoClient().github_data.ros_repo_4313,
MongoClient().github_data.ros_repo_4314,
MongoClient().github_data.ros_repo_4315,
MongoClient().github_data.ros_repo_4316,
MongoClient().github_data.ros_repo_4317,
MongoClient().github_data.ros_repo_4318,
MongoClient().github_data.ros_repo_4319,
MongoClient().github_data.ros_repo_4320,
MongoClient().github_data.ros_repo_4321,
MongoClient().github_data.ros_repo_4322,
MongoClient().github_data.ros_repo_4323,
MongoClient().github_data.ros_repo_4324,
MongoClient().github_data.ros_repo_4325,
MongoClient().github_data.ros_repo_4326,
MongoClient().github_data.ros_repo_4327,
MongoClient().github_data.ros_repo_4328,
MongoClient().github_data.ros_repo_4329,
MongoClient().github_data.ros_repo_4330,
MongoClient().github_data.ros_repo_4331,
MongoClient().github_data.ros_repo_4332,
MongoClient().github_data.ros_repo_4333,
MongoClient().github_data.ros_repo_4334,
MongoClient().github_data.ros_repo_4335,
MongoClient().github_data.ros_repo_4336,
MongoClient().github_data.ros_repo_4337,
MongoClient().github_data.ros_repo_4338,
MongoClient().github_data.ros_repo_4339,
MongoClient().github_data.ros_repo_4340,
MongoClient().github_data.ros_repo_4341,
MongoClient().github_data.ros_repo_4342,
MongoClient().github_data.ros_repo_4343,
MongoClient().github_data.ros_repo_4344,
MongoClient().github_data.ros_repo_4345,
MongoClient().github_data.ros_repo_4346,
MongoClient().github_data.ros_repo_4347,
MongoClient().github_data.ros_repo_4348,
MongoClient().github_data.ros_repo_4349,
MongoClient().github_data.ros_repo_4350,
MongoClient().github_data.ros_repo_4351,
MongoClient().github_data.ros_repo_4352,
MongoClient().github_data.ros_repo_4353,
MongoClient().github_data.ros_repo_4354,
MongoClient().github_data.ros_repo_4355,
MongoClient().github_data.ros_repo_4356,
MongoClient().github_data.ros_repo_4357,
MongoClient().github_data.ros_repo_4358,
MongoClient().github_data.ros_repo_4359,
MongoClient().github_data.ros_repo_4360,
MongoClient().github_data.ros_repo_4361,
MongoClient().github_data.ros_repo_4362,
MongoClient().github_data.ros_repo_4363,
MongoClient().github_data.ros_repo_4364,
MongoClient().github_data.ros_repo_4365,
MongoClient().github_data.ros_repo_4366,
MongoClient().github_data.ros_repo_4367,
MongoClient().github_data.ros_repo_4368,
MongoClient().github_data.ros_repo_4369,
MongoClient().github_data.ros_repo_4370,
MongoClient().github_data.ros_repo_4371,
MongoClient().github_data.ros_repo_4372,
MongoClient().github_data.ros_repo_4373,
MongoClient().github_data.ros_repo_4374,
MongoClient().github_data.ros_repo_4375,
MongoClient().github_data.ros_repo_4376,
MongoClient().github_data.ros_repo_4377,
MongoClient().github_data.ros_repo_4378,
MongoClient().github_data.ros_repo_4379,
MongoClient().github_data.ros_repo_4380,
MongoClient().github_data.ros_repo_4381,
MongoClient().github_data.ros_repo_4382,
MongoClient().github_data.ros_repo_4383,
MongoClient().github_data.ros_repo_4384,
MongoClient().github_data.ros_repo_4385,
MongoClient().github_data.ros_repo_4386,
MongoClient().github_data.ros_repo_4387,
MongoClient().github_data.ros_repo_4388,
MongoClient().github_data.ros_repo_4389,
MongoClient().github_data.ros_repo_4390,
MongoClient().github_data.ros_repo_4391,
MongoClient().github_data.ros_repo_4392,
MongoClient().github_data.ros_repo_4393,
MongoClient().github_data.ros_repo_4394,
MongoClient().github_data.ros_repo_4395,
MongoClient().github_data.ros_repo_4396,
MongoClient().github_data.ros_repo_4397,
MongoClient().github_data.ros_repo_4398,
MongoClient().github_data.ros_repo_4399,
MongoClient().github_data.ros_repo_4400,
MongoClient().github_data.ros_repo_4401,
MongoClient().github_data.ros_repo_4402,
MongoClient().github_data.ros_repo_4403,
MongoClient().github_data.ros_repo_4404,
MongoClient().github_data.ros_repo_4405,
MongoClient().github_data.ros_repo_4406,
MongoClient().github_data.ros_repo_4407,
MongoClient().github_data.ros_repo_4408,
MongoClient().github_data.ros_repo_4409,
MongoClient().github_data.ros_repo_4410,
MongoClient().github_data.ros_repo_4411,
MongoClient().github_data.ros_repo_4412,
MongoClient().github_data.ros_repo_4413,
MongoClient().github_data.ros_repo_4414,
MongoClient().github_data.ros_repo_4415,
MongoClient().github_data.ros_repo_4416,
MongoClient().github_data.ros_repo_4417,
MongoClient().github_data.ros_repo_4418,
MongoClient().github_data.ros_repo_4419,
MongoClient().github_data.ros_repo_4420,
MongoClient().github_data.ros_repo_4421,
MongoClient().github_data.ros_repo_4422,
MongoClient().github_data.ros_repo_4423,
MongoClient().github_data.ros_repo_4424,
MongoClient().github_data.ros_repo_4425,
MongoClient().github_data.ros_repo_4426,
MongoClient().github_data.ros_repo_4427,
MongoClient().github_data.ros_repo_4428,
MongoClient().github_data.ros_repo_4429,
MongoClient().github_data.ros_repo_4430,
MongoClient().github_data.ros_repo_4431,
MongoClient().github_data.ros_repo_4432,
MongoClient().github_data.ros_repo_4433,
MongoClient().github_data.ros_repo_4434,
MongoClient().github_data.ros_repo_4435,
MongoClient().github_data.ros_repo_4436,
MongoClient().github_data.ros_repo_4437,
MongoClient().github_data.ros_repo_4438,
MongoClient().github_data.ros_repo_4439,
MongoClient().github_data.ros_repo_4440,
MongoClient().github_data.ros_repo_4441,
MongoClient().github_data.ros_repo_4442,
MongoClient().github_data.ros_repo_4443,
MongoClient().github_data.ros_repo_4444,
MongoClient().github_data.ros_repo_4445,
MongoClient().github_data.ros_repo_4446,
MongoClient().github_data.ros_repo_4447,
MongoClient().github_data.ros_repo_4448,
MongoClient().github_data.ros_repo_4449,
MongoClient().github_data.ros_repo_4450,
MongoClient().github_data.ros_repo_4451,
MongoClient().github_data.ros_repo_4452,
MongoClient().github_data.ros_repo_4453,
MongoClient().github_data.ros_repo_4454,
MongoClient().github_data.ros_repo_4455,
MongoClient().github_data.ros_repo_4456,
MongoClient().github_data.ros_repo_4457,
MongoClient().github_data.ros_repo_4458,
MongoClient().github_data.ros_repo_4459,
MongoClient().github_data.ros_repo_4460,
MongoClient().github_data.ros_repo_4461,
MongoClient().github_data.ros_repo_4462,
MongoClient().github_data.ros_repo_4463,
MongoClient().github_data.ros_repo_4464,
MongoClient().github_data.ros_repo_4465,
MongoClient().github_data.ros_repo_4466,
MongoClient().github_data.ros_repo_4467,
MongoClient().github_data.ros_repo_4468,
MongoClient().github_data.ros_repo_4469,
MongoClient().github_data.ros_repo_4470,
MongoClient().github_data.ros_repo_4471,
MongoClient().github_data.ros_repo_4472,
MongoClient().github_data.ros_repo_4473,
MongoClient().github_data.ros_repo_4474,
MongoClient().github_data.ros_repo_4475,
MongoClient().github_data.ros_repo_4476,
MongoClient().github_data.ros_repo_4477,
MongoClient().github_data.ros_repo_4478,
MongoClient().github_data.ros_repo_4479,
MongoClient().github_data.ros_repo_4480,
MongoClient().github_data.ros_repo_4481,
MongoClient().github_data.ros_repo_4482,
MongoClient().github_data.ros_repo_4483,
MongoClient().github_data.ros_repo_4484,
MongoClient().github_data.ros_repo_4485,
MongoClient().github_data.ros_repo_4486,
MongoClient().github_data.ros_repo_4487,
MongoClient().github_data.ros_repo_4488,
MongoClient().github_data.ros_repo_4489,
MongoClient().github_data.ros_repo_4490,
MongoClient().github_data.ros_repo_4491,
MongoClient().github_data.ros_repo_4492,
MongoClient().github_data.ros_repo_4493,
MongoClient().github_data.ros_repo_4494,
MongoClient().github_data.ros_repo_4495,
MongoClient().github_data.ros_repo_4496,
MongoClient().github_data.ros_repo_4497,
MongoClient().github_data.ros_repo_4498,
MongoClient().github_data.ros_repo_4499,
MongoClient().github_data.ros_repo_4500,
MongoClient().github_data.ros_repo_4501,
MongoClient().github_data.ros_repo_4502,
MongoClient().github_data.ros_repo_4503,
MongoClient().github_data.ros_repo_4504,
MongoClient().github_data.ros_repo_4505,
MongoClient().github_data.ros_repo_4506,
MongoClient().github_data.ros_repo_4507,
MongoClient().github_data.ros_repo_4508,
MongoClient().github_data.ros_repo_4509,
MongoClient().github_data.ros_repo_4510,
MongoClient().github_data.ros_repo_4511,
MongoClient().github_data.ros_repo_4512,
MongoClient().github_data.ros_repo_4513,
MongoClient().github_data.ros_repo_4514,
MongoClient().github_data.ros_repo_4515,
MongoClient().github_data.ros_repo_4516,
MongoClient().github_data.ros_repo_4517,
MongoClient().github_data.ros_repo_4518,
MongoClient().github_data.ros_repo_4519,
MongoClient().github_data.ros_repo_4520,
MongoClient().github_data.ros_repo_4521,
MongoClient().github_data.ros_repo_4522,
MongoClient().github_data.ros_repo_4523,
MongoClient().github_data.ros_repo_4524,
MongoClient().github_data.ros_repo_4525,
MongoClient().github_data.ros_repo_4526,
MongoClient().github_data.ros_repo_4527,
MongoClient().github_data.ros_repo_4528,
MongoClient().github_data.ros_repo_4529,
MongoClient().github_data.ros_repo_4530,
MongoClient().github_data.ros_repo_4531,
MongoClient().github_data.ros_repo_4532,
MongoClient().github_data.ros_repo_4533,
MongoClient().github_data.ros_repo_4534,
MongoClient().github_data.ros_repo_4535,
MongoClient().github_data.ros_repo_4536,
MongoClient().github_data.ros_repo_4537,
MongoClient().github_data.ros_repo_4538,
MongoClient().github_data.ros_repo_4539,
MongoClient().github_data.ros_repo_4540,
MongoClient().github_data.ros_repo_4541,
MongoClient().github_data.ros_repo_4542,
MongoClient().github_data.ros_repo_4543,
MongoClient().github_data.ros_repo_4544,
MongoClient().github_data.ros_repo_4545,
MongoClient().github_data.ros_repo_4546,
MongoClient().github_data.ros_repo_4547,
MongoClient().github_data.ros_repo_4548,
MongoClient().github_data.ros_repo_4549,
MongoClient().github_data.ros_repo_4550,
MongoClient().github_data.ros_repo_4551,
MongoClient().github_data.ros_repo_4552,
MongoClient().github_data.ros_repo_4553,
MongoClient().github_data.ros_repo_4554,
MongoClient().github_data.ros_repo_4555,
MongoClient().github_data.ros_repo_4556,
MongoClient().github_data.ros_repo_4557,
MongoClient().github_data.ros_repo_4558,
MongoClient().github_data.ros_repo_4559,
MongoClient().github_data.ros_repo_4560,
MongoClient().github_data.ros_repo_4561,
MongoClient().github_data.ros_repo_4562,
MongoClient().github_data.ros_repo_4563,
MongoClient().github_data.ros_repo_4564,
MongoClient().github_data.ros_repo_4565,
MongoClient().github_data.ros_repo_4566,
MongoClient().github_data.ros_repo_4567,
MongoClient().github_data.ros_repo_4568,
MongoClient().github_data.ros_repo_4569,
MongoClient().github_data.ros_repo_4570,
MongoClient().github_data.ros_repo_4571,
MongoClient().github_data.ros_repo_4572,
MongoClient().github_data.ros_repo_4573,
MongoClient().github_data.ros_repo_4574,
MongoClient().github_data.ros_repo_4575,
MongoClient().github_data.ros_repo_4576,
MongoClient().github_data.ros_repo_4577,
MongoClient().github_data.ros_repo_4578,
MongoClient().github_data.ros_repo_4579,
MongoClient().github_data.ros_repo_4580,
MongoClient().github_data.ros_repo_4581,
MongoClient().github_data.ros_repo_4582,
MongoClient().github_data.ros_repo_4583,
MongoClient().github_data.ros_repo_4584,
MongoClient().github_data.ros_repo_4585,
MongoClient().github_data.ros_repo_4586,
MongoClient().github_data.ros_repo_4587,
MongoClient().github_data.ros_repo_4588,
MongoClient().github_data.ros_repo_4589,
MongoClient().github_data.ros_repo_4590,
MongoClient().github_data.ros_repo_4591,
MongoClient().github_data.ros_repo_4592,
MongoClient().github_data.ros_repo_4593,
MongoClient().github_data.ros_repo_4594,
MongoClient().github_data.ros_repo_4595,
MongoClient().github_data.ros_repo_4596,
MongoClient().github_data.ros_repo_4597,
MongoClient().github_data.ros_repo_4598,
MongoClient().github_data.ros_repo_4599,
MongoClient().github_data.ros_repo_4600,
MongoClient().github_data.ros_repo_4601,
MongoClient().github_data.ros_repo_4602,
MongoClient().github_data.ros_repo_4603,
MongoClient().github_data.ros_repo_4604,
MongoClient().github_data.ros_repo_4605,
MongoClient().github_data.ros_repo_4606,
MongoClient().github_data.ros_repo_4607,
MongoClient().github_data.ros_repo_4608,
MongoClient().github_data.ros_repo_4609,
MongoClient().github_data.ros_repo_4610,
MongoClient().github_data.ros_repo_4611,
MongoClient().github_data.ros_repo_4612,
MongoClient().github_data.ros_repo_4613,
MongoClient().github_data.ros_repo_4614,
MongoClient().github_data.ros_repo_4615,
MongoClient().github_data.ros_repo_4616,
MongoClient().github_data.ros_repo_4617,
MongoClient().github_data.ros_repo_4618,
MongoClient().github_data.ros_repo_4619,
MongoClient().github_data.ros_repo_4620,
MongoClient().github_data.ros_repo_4621,
MongoClient().github_data.ros_repo_4622,
MongoClient().github_data.ros_repo_4623,
MongoClient().github_data.ros_repo_4624,
MongoClient().github_data.ros_repo_4625,
MongoClient().github_data.ros_repo_4626,
MongoClient().github_data.ros_repo_4627,
MongoClient().github_data.ros_repo_4628,
MongoClient().github_data.ros_repo_4629,
MongoClient().github_data.ros_repo_4630,
MongoClient().github_data.ros_repo_4631,
MongoClient().github_data.ros_repo_4632,
MongoClient().github_data.ros_repo_4633,
MongoClient().github_data.ros_repo_4634,
MongoClient().github_data.ros_repo_4635,
MongoClient().github_data.ros_repo_4636,
MongoClient().github_data.ros_repo_4637,
MongoClient().github_data.ros_repo_4638,
MongoClient().github_data.ros_repo_4639,
MongoClient().github_data.ros_repo_4640,
MongoClient().github_data.ros_repo_4641,
MongoClient().github_data.ros_repo_4642,
MongoClient().github_data.ros_repo_4643,
MongoClient().github_data.ros_repo_4644,
MongoClient().github_data.ros_repo_4645,
MongoClient().github_data.ros_repo_4646,
MongoClient().github_data.ros_repo_4647,
MongoClient().github_data.ros_repo_4648,
MongoClient().github_data.ros_repo_4649,
MongoClient().github_data.ros_repo_4650,
MongoClient().github_data.ros_repo_4651,
MongoClient().github_data.ros_repo_4652,
MongoClient().github_data.ros_repo_4653,
MongoClient().github_data.ros_repo_4654,
MongoClient().github_data.ros_repo_4655,
MongoClient().github_data.ros_repo_4656,
MongoClient().github_data.ros_repo_4657,
MongoClient().github_data.ros_repo_4658,
MongoClient().github_data.ros_repo_4659,
MongoClient().github_data.ros_repo_4660,
MongoClient().github_data.ros_repo_4661,
MongoClient().github_data.ros_repo_4662,
MongoClient().github_data.ros_repo_4663,
MongoClient().github_data.ros_repo_4664,
MongoClient().github_data.ros_repo_4665,
MongoClient().github_data.ros_repo_4666,
MongoClient().github_data.ros_repo_4667,
MongoClient().github_data.ros_repo_4668,
MongoClient().github_data.ros_repo_4669,
MongoClient().github_data.ros_repo_4670,
MongoClient().github_data.ros_repo_4671,
MongoClient().github_data.ros_repo_4672,
MongoClient().github_data.ros_repo_4673,
MongoClient().github_data.ros_repo_4674,
MongoClient().github_data.ros_repo_4675,
MongoClient().github_data.ros_repo_4676,
MongoClient().github_data.ros_repo_4677,
MongoClient().github_data.ros_repo_4678,
MongoClient().github_data.ros_repo_4679,
MongoClient().github_data.ros_repo_4680,
MongoClient().github_data.ros_repo_4681,
MongoClient().github_data.ros_repo_4682,
MongoClient().github_data.ros_repo_4683,
MongoClient().github_data.ros_repo_4684,
MongoClient().github_data.ros_repo_4685,
MongoClient().github_data.ros_repo_4686,
MongoClient().github_data.ros_repo_4687,
MongoClient().github_data.ros_repo_4688,
MongoClient().github_data.ros_repo_4689,
MongoClient().github_data.ros_repo_4690,
MongoClient().github_data.ros_repo_4691,
MongoClient().github_data.ros_repo_4692,
MongoClient().github_data.ros_repo_4693,
MongoClient().github_data.ros_repo_4694,
MongoClient().github_data.ros_repo_4695,
MongoClient().github_data.ros_repo_4696,
MongoClient().github_data.ros_repo_4697,
MongoClient().github_data.ros_repo_4698,
MongoClient().github_data.ros_repo_4699,
MongoClient().github_data.ros_repo_4700]

repo_info_array = [
    'db_id',
    'name',
    'age',
    'tags',
    'created_at',
    'owner',
    'ofc',
    'language',
    'contributors',
    'forks',
    'stars',
    'watch',
    'issues_count',
    'issues_closed',
    'commits_count',
    'total_issues_comments_count',
    'avg_issues_comments_count',
    'issues_reviewed',
    'avg_commits_per_pr',
    'avg_repo_sentiment_score',
    'avg_repo_sentiment_label',
    'avg_issue_sentiment_score',
    'avg_issue_sentiment_label',
    'avg_line_addition',
    'avg_line_deletion',
    'avg_line_addition_issues_with_comments',
    'avg_line_deletion_issues_with_comments',
    'avg_line_addition_issues_without_comments',
    'avg_line_deletion_issues_without_comments',
    'commits_before_initial_issue',
    'days_before_initial_issue',
    'avg_days_between_issues',
    'avg_commits_between_issues',
    'sec_to_close',
    'avg_secs_before_issue_closes',
    'avg_sec_before_issue_with_comments_closes',
    'avg_sec_before_issue_without_comments_closes',
    'avg_issue_openers_followers_count',
    'avg_issue_closers_followers_count',
    'avg_reviewers_count_per_issue',
    'avg_reviewers_count_per_reviewed_issue',
    'avg_minutes_to_commit',
]


# to export the events sorted by date to a spread sheet
def export_time_line_data(entry, sheet1, row, db_id):

    # results = xlwt.Workbook(encoding="utf-8")
    # sheet1 = results.add_sheet('TimeLine')

    # col = 0
    # for i in range(0, len(repo_info_array)):
    #     sheet1.write(0, col, str(repo_info_array[i]))
    #     col += 1
    if entry.get('time_line'):
        tgg = ''
        if entry.get('topics') is not None:
            for tg in range (0, len(entry['topics']['names'])):
                tgg += entry['topics']['names'][tg] + ','
        print entry['urls']['repo_url']
        name = entry['name']
        created_at = entry['created_at']
        tags = tgg
        age = Utility.repos_age(created_at)
        owner = entry['owner']
        ofc = entry['owner_followers_count']
        language = entry['language']
        contributors = entry['contributors_count']
        forks = entry['popularity']['forks']
        stars = entry['popularity']['stars']
        watch = entry['popularity']['watch']
        issues_count = entry['statistics']['total_issues']
        issues_closed = entry['statistics']['total_closed_issues']
        commits_count = entry['statistics']['total_commits']
        total_issues_comments_count = entry['statistics']['total_issues_comments']
        avg_issues_comments_count = 0 if issues_count == 0 else total_issues_comments_count / float(issues_count)

        time_line_array = entry['time_line']
        sorted_time_line = sorted(time_line_array, key=lambda l: l['created_at'])

        from_time_line = process_time_line(created_at, sorted_time_line)

        issues_reviewed = from_time_line['issues_reviewed']
        avg_commits_per_pr = 0 if issues_count == 0 else float(from_time_line['total_commits_per_pr']) / float(issues_count)
        repo_sentiment_score_array = from_time_line['repo_sentiment_score_array']
        issue_sentiment_score_array = from_time_line['issue_sentiment_score_array']

        if total_issues_comments_count > 0:
            avg_repo_sentiment_score = sum(from_time_line['repo_sentiment_score_array']) / float(total_issues_comments_count)
            avg_repo_sentiment_label = Utility.sentiment_label(avg_repo_sentiment_score)
            avg_issue_sentiment_score = sum(from_time_line['issue_sentiment_score_array']) / float(issues_reviewed)
            avg_issue_sentiment_label = Utility.sentiment_label(avg_issue_sentiment_score)
        else:
            avg_repo_sentiment_score = 0
            avg_repo_sentiment_label = None
            avg_issue_sentiment_score = 0
            avg_issue_sentiment_label = None

        avg_line_addition = 0 if issues_count == 0 else from_time_line['total_line_addition'] / float(issues_count)
        avg_line_deletion = 0 if issues_count == 0 else from_time_line['total_line_deletion'] / float(issues_count)
        avg_line_addition_issues_with_comments = 0 if issues_reviewed == 0 else from_time_line['total_line_addition_issues_with_comments'] / float(issues_reviewed)
        avg_line_deletion_issues_with_comments = 0 if issues_reviewed == 0 else from_time_line['total_line_deletion_issues_with_comments'] / float(issues_reviewed)
        avg_line_addition_issues_without_comments = 0 if issues_count-issues_reviewed == 0 else from_time_line['total_line_addition_issues_without_comments'] / float(issues_count - issues_reviewed)
        avg_line_deletion_issues_without_comments = 0 if issues_count-issues_reviewed == 0 else from_time_line['total_line_deletion_issues_without_comments'] / float(issues_count - issues_reviewed)
        days_before_initial_issue = from_time_line['days_before_initial_issue']
        days_between_issues = from_time_line['days_between_issues']
        commits_between_issues = from_time_line['commits_between_issues']

        avg_secs_before_issue_closes = 0 if issues_closed == 0 else sum(from_time_line['secs_before_issue_closes']) / float(issues_closed)
        secs_before_issue_with_comments_closes = from_time_line['secs_before_issue_with_comments_closes']
        secs_before_issue_without_comments_closes = from_time_line['secs_before_issue_without_comments_closes']
        avg_secs_before_issue_with_comments_closes = None if issues_reviewed == 0 else sum(secs_before_issue_with_comments_closes) / float(issues_reviewed)
        avg_secs_before_issue_without_comments_closes = 0 if (issues_closed - issues_reviewed) <= 0 else sum(secs_before_issue_without_comments_closes) / float(issues_closed - issues_reviewed)
        avg_issue_opener_fc = 0 if issues_count == 0 else sum(from_time_line['issue_opener_fc'])/float(issues_count)
        avg_issue_closer_fc = None if len(from_time_line['issue_closer_fc']) == 0 else sum(from_time_line['issue_closer_fc'])/float(issues_closed)

        reviewers_count = from_time_line['reviewers_count']
        min_to_commit = from_time_line['min_to_commit']
        e = {
            'db_id': db_id,
            'name': name,
            'age': age,
            'tags': tags,
            'created_at': entry['created_at'],
            'owner': owner,
            'ofc': ofc,
            'language': language,
            'contributors': contributors,
            'forks': forks,
            'stars': stars,
            'watch': watch,
            'issues_count': issues_count,
            'issues_closed': issues_closed,
            'commits_count': from_time_line['commits_count'],
            'total_issues_comments_count': total_issues_comments_count,
            'avg_issues_comments_count': avg_issues_comments_count,
            'issues_reviewed': issues_reviewed,
            'avg_commits_per_pr': avg_commits_per_pr,
            'repo_sentiment_score_array': repo_sentiment_score_array,
            'avg_repo_sentiment_score': avg_repo_sentiment_score,
            'avg_repo_sentiment_label': avg_repo_sentiment_label,
            'issue_sentiment_score_array': issue_sentiment_score_array,
            'avg_issue_sentiment_score': avg_issue_sentiment_score,
            'avg_issue_sentiment_label': avg_issue_sentiment_label,
            'avg_line_addition': avg_line_addition,
            'avg_line_deletion': avg_line_deletion,
            'avg_line_addition_issues_with_comments': avg_line_addition_issues_with_comments,
            'avg_line_deletion_issues_with_comments': avg_line_deletion_issues_with_comments,
            'avg_line_addition_issues_without_comments': avg_line_addition_issues_without_comments,
            'avg_line_deletion_issues_without_comments': avg_line_deletion_issues_without_comments,
            'commits_before_initial_issue': 0 if len(commits_between_issues) == 0 else commits_between_issues[0],
            'days_before_initial_issue': days_before_initial_issue,
            'days_between_issues': days_between_issues,
            'avg_days_between_issues': 0 if (issues_count-1) == 0 else (sum(days_between_issues)/float(issues_count-1))/86400,
            'commits_between_issues': commits_between_issues[1:],
            'avg_commits_between_issues': 0 if (issues_count-1) ==0 else sum(commits_between_issues[1:]) / float(issues_count-1),
            'sec_to_close': [],
            'avg_secs_before_issue_closes': avg_secs_before_issue_closes,
            'avg_sec_before_issue_with_comments_closes': avg_secs_before_issue_with_comments_closes,
            'avg_sec_before_issue_without_comments_closes': avg_secs_before_issue_without_comments_closes,
            'avg_issue_openers_followers_count': avg_issue_opener_fc,
            'avg_issue_closers_followers_count': avg_issue_closer_fc,
            'reviewers_count_per_issue': reviewers_count,
            'avg_reviewers_count_per_issue': 0 if issues_count == 0 else sum(reviewers_count) / float(issues_count),
            'avg_reviewers_count_per_reviewed_issue': 0 if issues_reviewed == 0 else sum(reviewers_count) / float(issues_reviewed),
            'minutes_to_commit': min_to_commit,
            'avg_minutes_to_commit': sum(min_to_commit) / float(commits_count),
            'total_addition': from_time_line['addition'],
            'total_deletion': from_time_line['deletion']
        }

        export_to_sheet(e, sheet1, row)


def process_time_line(repo_created_at, repo_time_line):

    issues_reviewed = 0
    total_commits_per_pr = 0
    repo_sentiment_score_array = []
    issue_sentiment_score_array = []
    total_line_addition = 0
    total_line_deletion = 0
    total_line_addition_issues_with_comments = 0
    total_line_deletion_issues_with_comments = 0
    total_line_addition_issues_without_comments = 0
    total_line_deletion_issues_without_comments = 0

    addition_array = []
    deletion_array = []

    first_commit_date = repo_time_line[0]['created_at']

    issue_opened_date = []
    commits_between_issues = []
    commits_between_issues_count = 0
    commits_count = 0

    secs_to_close = []
    sec_to_close_with_comments = []
    sec_to_close_without_comments = []

    issue_openers_fc = []
    issue_closers_fc = []

    reviewers_count_array = []
    commit_1_date = first_commit_date
    min_to_commit = []

    for entry in repo_time_line:
        if entry['type'] == 'IssueOpened':
            issue_opened_date.append(entry['created_at'])
            commits_between_issues.append(commits_between_issues_count)
            commits_between_issues_count = 0
            issue_openers_fc.append(entry['author_followers_count'])
            if entry['comments_count'] > 0:
                if entry['isClosed']:
                    if entry.get('seconds_to_close'):
                        sec_to_close_with_comments.append(entry['seconds_to_close'])
                issues_reviewed += 1
                issue_sentiment_score = 0
                reviewers = []
                reviewers_count = 0

                for cmnt in entry['comments']:
                    if cmnt['author'] not in reviewers:
                        reviewers.append(cmnt['author'])
                        reviewers_count += 1

                    repo_sentiment_score_array.append(cmnt['sentiment_score'])
                    issue_sentiment_score += cmnt['sentiment_score']

                issue_sentiment_score_array.append(float(issue_sentiment_score)/float(entry['comments_count']))
                reviewers_count_array.append(reviewers_count)

                if entry.get('addition'):
                    total_line_addition_issues_with_comments += entry['addition']
                if entry.get('deletion'):
                    total_line_deletion_issues_with_comments += entry['deletion']
            else:
                reviewers_count_array.append(0)
                if entry['isClosed']:
                    if entry.get('seconds_to_close'):
                        sec_to_close_without_comments.append(entry['seconds_to_close'])

                if entry.get('addition'):
                    total_line_addition_issues_without_comments += entry['addition']
                if entry.get('deletion'):
                    total_line_deletion_issues_without_comments += entry['deletion']

            if entry.get('commits_count'):
                total_commits_per_pr += entry['commits_count']
            if entry.get('addition'):
                total_line_addition += entry['addition']
            if entry.get('deletion'):
                total_line_deletion += entry['deletion']

            if entry['isClosed']:
                if entry.get('seconds_to_close'):
                    secs_to_close.append(entry['seconds_to_close'])

            if entry.get('addition'):
                addition_array.append(entry['addition'])
            if entry.get('deletion'):
                deletion_array.append(entry['deletion'])

        elif entry['type'] == 'Commit':
            commits_count += 1
            commit_2_date = entry['created_at']
            min_to_commit.append(Utility.time_diff_sec(commit_1_date,commit_2_date)/60)
            commit_1_date = commit_2_date
            commits_between_issues_count += 1
        else:
            issue_closers_fc.append(entry['author_followers_count'])

    dates = [datetime.datetime.strptime(ts, '%Y-%m-%dT%H:%M:%SZ') for ts in issue_opened_date]
    dates.sort()
    sorteddates = [datetime.datetime.strftime(ts, '%Y-%m-%dT%H:%M:%SZ') for ts in dates]

    days_between_issues = []
    for dt in range(0, len(sorteddates)-1):
        days_between_issues.append(Utility.time_diff(sorteddates[dt], sorteddates[dt+1]))

    days_before_initial_issue = 0 if len(sorteddates) == 0 else Utility.time_diff_day(repo_created_at, sorteddates[0])

    returned = {
        'issues_reviewed': issues_reviewed,
        'total_commits_per_pr': total_commits_per_pr,
        'repo_sentiment_score_array': repo_sentiment_score_array,
        'issue_sentiment_score_array': issue_sentiment_score_array,
        'total_line_addition': total_line_addition,
        'total_line_deletion': total_line_deletion,
        'total_line_addition_issues_without_comments': total_line_addition_issues_without_comments,
        'total_line_deletion_issues_without_comments': total_line_deletion_issues_without_comments,
        'total_line_addition_issues_with_comments': total_line_addition_issues_with_comments,
        'total_line_deletion_issues_with_comments': total_line_deletion_issues_with_comments,
        'days_before_initial_issue': days_before_initial_issue,
        'days_between_issues': days_between_issues,
        'commits_between_issues': commits_between_issues,
        'secs_before_issue_closes': secs_to_close,
        'secs_before_issue_with_comments_closes': sec_to_close_with_comments,
        'secs_before_issue_without_comments_closes': sec_to_close_without_comments,
        'issue_opener_fc': issue_openers_fc,
        'issue_closer_fc': issue_closers_fc,
        'reviewers_count': reviewers_count_array,
        'min_to_commit': min_to_commit,
        'commits_count': commits_count,
        'addition': addition_array,
        'deletion': deletion_array
    }

    return returned


def export_to_sheet(entry, sheet, row):

    col = 0
    for i in range(0, len(repo_info_array)):
        sheet.write(row, col, str(entry[repo_info_array[i]]))
        col += 1


# The main function
if __name__ == "__main__":

    results = xlwt.Workbook(encoding="utf-8")
    sheet1 = results.add_sheet('TimeLine_ros')

    col = 0
    for i in range(0, len(repo_info_array)):
        sheet1.write(0, col, str(repo_info_array[i]))
        col += 1

    row = 1
    db_id = 4301
    for k in range(0, len(db_list)):
        try:
            count = db_list[k].count()
            if count > 0:
                main_entry = db_list[k].find()[count - 1]
                if main_entry.get('contributors_count'):

                    new_entry = []
                    comm_array = []

                    for com in db_list[k].find():
                        if com.get('type') == 'Comment':
                            comm_array.append(com)

                    j = 0
                    for e in db_list[k].find():
                        j+=1
                        if not e.get('contributors_count') and e.get('type') != 'Comment':
                            if e.get('type') == 'IssueOpened':
                                issue_comments = []
                                e['comments'] = {}
                                issue_num = e['issue_number']
                                for i in range(0,len(comm_array)):
                                    comm_issue_num = comm_array[i].get('issue_number')
                                    if issue_num == comm_issue_num:
                                        issue_comments.append(comm_array[i])
                                if len(issue_comments) != 0:
                                    e['comments'] = issue_comments
                            new_entry.append(e)
                        print str(k)+ ' - '+str(j)+'/'+str(count)

                    main_entry['time_line'] = new_entry
                    # pprint.pprint(main_entry)
                    export_time_line_data(main_entry, sheet1, row, db_id)
                    row+=1
                    print str(k) + ' is done'
                    results.save("ros_4301_4700.xls")
                else:
                    print str(k) + ' is not a complete processed repository'
        except Exception as er:
            print er.message
        db_id += 1
