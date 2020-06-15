import pprint
import sys
from datetime import datetime
import xlwt
from textblob import TextBlob
import json
import time
from pymongo import MongoClient
import Utility

__author__ = 'Abduljaleel Al Rubaye'

final_time_line_db = MongoClient().github_data.final_time_line

repo_info_array = [
    'name',
    'age',
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
    'avg_minutes_to_commit:',
]


# to export the events sorted by date to a spread sheet
def export_time_line_data():

    results = xlwt.Workbook(encoding="utf-8")
    sheet1 = results.add_sheet('TimeLine')

    col = 0
    for i in range(0, len(repo_info_array)):
        sheet1.write(0, col, str(repo_info_array[i]))
        col += 1

    row = 1
    ii = 1
    for entry in final_time_line_db.find():

        print entry['urls']['repo_url']
        name = entry['name']
        created_at = entry['created_at']
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
        avg_issues_comments_count = total_issues_comments_count / float(issues_count)
        from_time_line = process_time_line(entry['time_line'])
        issues_reviewed = from_time_line['issues_reviewed']
        avg_commits_per_pr = float(from_time_line['total_commits_per_pr']) / float(issues_count)
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

        avg_line_addition = from_time_line['total_line_addition'] / float(issues_count)
        avg_line_deletion = from_time_line['total_line_deletion'] / float(issues_count)
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
        avg_issue_opener_fc = sum(from_time_line['issue_opener_fc'])/float(issues_count)
        avg_issue_closer_fc = None if len(from_time_line['issue_closer_fc']) == 0 else sum(from_time_line['issue_closer_fc'])/float(issues_closed)

        reviewers_count = from_time_line['reviewers_count']
        min_to_commit = from_time_line['min_to_commit']

        e = {
            'name': name,
            'age': age,
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
            'commits_before_initial_issue': commits_between_issues[0],
            'days_before_initial_issue': days_before_initial_issue,
            'days_between_issues': days_between_issues,
            'avg_days_between_issues': 0 if (issues_count-1) == 0 else sum(days_between_issues)/float(issues_count-1),
            'commits_between_issues': commits_between_issues[1:],
            'avg_commits_between_issues': 0 if (issues_count-1) ==0 else sum(commits_between_issues[1:]) / float(issues_count-1),
            'sec_to_close': from_time_line['secs_before_issue_closes'],
            'avg_secs_before_issue_closes': avg_secs_before_issue_closes,
            'avg_sec_before_issue_with_comments_closes': avg_secs_before_issue_with_comments_closes,
            'avg_sec_before_issue_without_comments_closes': avg_secs_before_issue_without_comments_closes,
            'avg_issue_openers_followers_count': avg_issue_opener_fc,
            'avg_issue_closers_followers_count': avg_issue_closer_fc,
            'reviewers_count_per_issue':reviewers_count,
            'avg_reviewers_count_per_issue': sum(reviewers_count) / float(issues_count),
            'avg_reviewers_count_per_reviewed_issue': 0 if issues_reviewed == 0 else sum(reviewers_count) / float(issues_reviewed),
            'minutes_to_commit': min_to_commit,
            'avg_minutes_to_commit:': sum(min_to_commit) / float(commits_count),
            'total_addition': from_time_line['addition'],
            'total_deletion': from_time_line['deletion']
        }

        # pprint.pprint(e)

        export_to_sheet(e, sheet1, row)
        row += 1

        # # break
        # if ii > 5:
        #     break
        #
        # ii += 1

    results.save("pr_time_line_results.xls")


def process_time_line(repo_time_line):

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

    days_before_initial_issue = Utility.time_diff(first_commit_date, issue_opened_date[0])

    days_between_issues = []
    for dt in range(0, len(issue_opened_date)-1):
        days_between_issues.append(Utility.time_diff(issue_opened_date[dt], issue_opened_date[dt+1]))

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
    export_time_line_data()
