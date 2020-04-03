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


# to export the events sorted by date to a spread sheet
def export_time_line_data():
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
        avg_issues_comments_count = total_issues_comments_count / issues_count
        from_time_line = process_time_line(entry['time_line'])
        issues_reviewed = from_time_line['issues_reviewed']
        avg_commits_per_pr = float(from_time_line['total_commits_per_pr']) / float(issues_count)
        total_sentiment_score_array = from_time_line['total_sentiment_score_array']
        issue_sentiment_score_array = from_time_line['issue_sentiment_score_array']

        if total_issues_comments_count > 0:
            avg_total_sentiment_score = sum(from_time_line['total_sentiment_score_array']) / float(total_issues_comments_count)
            avg_total_sentiment_label = Utility.sentiment_label(avg_total_sentiment_score)
            avg_issue_sentiment_score = sum(from_time_line['issue_sentiment_score_array']) / float(issues_count)
            avg_issue_sentiment_label = Utility.sentiment_label(avg_issue_sentiment_score)
        else:
            avg_total_sentiment_score = 0
            avg_total_sentiment_label = None
            avg_issue_sentiment_score = 0
            avg_issue_sentiment_label = None

        avg_line_addition = from_time_line['total_line_addition'] / float(issues_count)
        avg_line_deletion = from_time_line['total_line_deletion'] / float(issues_count)
        days_before_initial_issue = from_time_line['days_before_initial_issue']
        days_between_issues = from_time_line['days_between_issues']
        commits_between_issues = from_time_line['commits_between_issues']

        avg_secs_before_issue_closes = 0 if issues_closed == 0 else sum (from_time_line['secs_before_issue_closes']) / float(issues_closed)
        secs_before_issue_with_comments_closes = from_time_line['secs_before_issue_with_comments_closes']
        secs_before_issue_without_comments_closes = from_time_line['secs_before_issue_without_comments_closes']
        avg_secs_before_issue_with_comments_closes = None if len(secs_before_issue_with_comments_closes) == 0 else sum(secs_before_issue_with_comments_closes) / float(issues_reviewed)
        avg_secs_before_issue_without_comments_closes = 0 if (issues_closed - issues_reviewed) <= 0 else sum(secs_before_issue_without_comments_closes) / float(issues_closed - issues_reviewed)
        avg_issue_opener_fc = sum(from_time_line['issue_opener_fc'])/float(issues_count)
        avg_issue_closer_fc = None if len(from_time_line['issue_closer_fc']) == 0 else sum(from_time_line['issue_closer_fc'])/float(issues_closed)

        reviewers_count = from_time_line['reviewers_count']
        min_to_commit = from_time_line['min_to_commit']

        e = {
            '01-name': name,
            '02-age': age,
            '03-owner': owner,
            '04-ofc': ofc,
            '05-language': language,
            '06-contributors': contributors,
            '07-forks': forks,
            '08-stars': stars,
            '09-watch': watch,
            '10-issues_count': issues_count,
            '11-issues_closed': issues_closed,
            '12-commits_count': from_time_line['commits_count'],
            '13-total_issues_comments_count': total_issues_comments_count,
            '14-avg_issues_comments_count': avg_issues_comments_count,
            '15-issues_reviewed': issues_reviewed,
            '16-avg_commits_per_pr': avg_commits_per_pr,
            '17-total_sentiment_score_array': total_sentiment_score_array,
            '18-avg_total_sentiment_score': avg_total_sentiment_score,
            '19-avg_total_sentiment_label': avg_total_sentiment_label,
            '20-issue_sentiment_score_array': issue_sentiment_score_array,
            '21-avg_issue_sentiment_score': avg_issue_sentiment_score,
            '22-avg_issue_sentiment_label': avg_issue_sentiment_label,
            '23-avg_line_addition': avg_line_addition,
            '24-avg_line_deletion': avg_line_deletion,
            '25-commits_before_initial_issue': commits_between_issues[0],
            '26-days_before_initial_issue': days_before_initial_issue,
            '27-days_between_issues': days_between_issues,
            '28-avg_days_between_issues': 0 if (issues_count-1) == 0 else sum(days_between_issues)/float(issues_count-1),
            '29-commits_between_issues': commits_between_issues[1:],
            '30-avg_commits_between_issues': 0 if (issues_count-1) ==0 else sum(commits_between_issues[1:]) / float(issues_count-1),
            '31-avg_secs_before_issue_closes': avg_secs_before_issue_closes,
            '32-avg_sec_before_issue_with_comments_closes': avg_secs_before_issue_with_comments_closes,
            '33-avg_sec_before_issue_without_comments_closes': avg_secs_before_issue_without_comments_closes,
            '34-avg_issue_openers_followers_count': avg_issue_opener_fc,
            '35-avg_issue_closers_followers_count': avg_issue_closer_fc,
            '36-reviewers_count_per_issue':reviewers_count,
            '37-avg_reviewers_count_per_issue': sum(reviewers_count) / float(issues_count),
            '38-avg_reviewers_count_per_reviewed_issue': 0 if issues_reviewed == 0 else sum(reviewers_count) / float(issues_reviewed),
            # '38-avg_commits_before_issue_closes':
            # '39-avg_commits_before_issue_with_comments_closes':
            # '40-avg_commits_before_issue_without_comments_closes':
            '41-minutes_to_commit': min_to_commit,
            '42-avg_minutes_to_commit:': sum(min_to_commit) / float(commits_count)
        }

        pprint.pprint(e)
        break
        # if ii > 50:
        #     break
        # ii+=1

# lines_added/deleted_ before the first issue


def process_time_line(repo_time_line):

    issues_reviewed = 0
    total_commits_per_pr = 0
    total_sentiment_score_array = []
    issue_sentiment_score_array = []
    total_line_addition = 0
    total_line_deletion = 0
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
                    sec_to_close_with_comments.append(entry['seconds_to_close'])
                issues_reviewed += 1
                issue_sentiment_score = 0
                reviewers = []
                reviewers_count = 0

                for cmnt in entry['comments']:
                    if cmnt['author'] not in reviewers:
                        reviewers.append(cmnt['author'])
                        reviewers_count += 1

                    total_sentiment_score_array.append(cmnt['sentiment_score'])
                    issue_sentiment_score += cmnt['sentiment_score']

                issue_sentiment_score_array.append(float(issue_sentiment_score)/float(entry['comments_count']))
                reviewers_count_array.append(reviewers_count)
            else:
                reviewers_count_array.append(0)
                if entry['isClosed']:
                    sec_to_close_without_comments.append(entry['seconds_to_close'])

            total_commits_per_pr += entry['commits_count']
            total_line_addition += entry['addition']
            total_line_deletion += entry['deletion']

            if entry['isClosed']:
                secs_to_close.append(entry['seconds_to_close'])

        elif entry['type'] == 'Commit':
            commits_count += 1
            commit_2_date = entry['created_at']
            print commit_2_date
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
        'total_sentiment_score_array': total_sentiment_score_array,
        'issue_sentiment_score_array': issue_sentiment_score_array,
        'total_line_addition': total_line_addition,
        'total_line_deletion': total_line_deletion,
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
        'commits_count': commits_count
    }

    return returned


# The main function
if __name__ == "__main__":
    export_time_line_data()


    # results = xlwt.Workbook(encoding="utf-8")

    # sheet1 = results.add_sheet('h')
    # row = 0

    #
    #     entry_type = entry['type']
    #     col_date = entry['created_at']
    #     sha = ''
    #     author = entry ['author']
    #     message = ''
    #     issue_num = entry['issue_number']
    #     if 'Issue' in entry_type:
    #         issue_num = entry['issue_number']
    #         if 'Opened' in entry_type:
    #             message = entry['title']
    #
    #     else:
    #         sha = entry['sha']
    #         message = entry['message']
    #
    #     sheet1.write(row, 0, entry_type)
    #     sheet1.write(row, 1, sha)
    #     sheet1.write(row, 2, author)
    #     sheet1.write(row, 3, message)
    #     sheet1.write(row, 4, col_date)
    #     sheet1.write(row, 5, issue_num)
    #
    #     row += 1
    #
    # results.save("pr_time_line_results.xls")
