import json
import pprint
import urllib2
from datetime import datetime
import time
import simplejson
from pymongo import MongoClient
import urllib

__author__ = 'Abdul Rubaye'

client = MongoClient()
database = client.github_data
repos = database.repos
pull_requests = database.pull_requests
events = database.events
commits = database.commits.bson
commit_comments = database.commit_comments
global time_line_array, issue_numbers_temp_array, api_call, start
global repo_commits_count, repo_issues_count, repo_closed_issues_count, repo_commits_comments_count, repo_issues_comments_count
global commits_positive_comments_count, commits_negative_comments_count, issues_positive_comments_count, issues_negative_comments_count
global commits_pos_comments_prob_sum, commits_neg_comments_prob_sum, commits_neutral_comments_prob_sum
global issues_pos_comments_prob_sum, issues_neg_comments_prob_sum, issues_neutral_comments_prob_sum

# client id and client secret are used in calling the github API
# they will help to raise the maximum limit of calls per hour
# note: you will need your private txt file that includes the private keys
privateVar = open("privateVar.txt", 'r').read()
client_id = privateVar.split('\n', 1)[0]
client_secret = privateVar.split('\n', 1)[1]


# fetch how many more calls we have for the hour
def git_api_rate_limit():
    data = fetch(add_url_query("https://api.github.com/rate_limit", 1), False)
    return data['rate']['remaining']


# appends the client id and the client secret to urls
def add_url_query(url, page):
    query = '?per_page=100&page=' + str(page) + '&client_id=' + client_id + '&client_secret=' + client_secret
    if len(url) == 1:
        return url[0] + query
    else:
        return url + query


# Returns data from a call to a url
def fetch(url, count_call):
    global api_call
    try:
        request = urllib2.Request(url, headers={"Accept": "application/vnd.github.v3.star+json"})
        response = urllib2.urlopen(request)
        data = simplejson.load(response)
        if count_call:
            api_call += 1
        return data
    except urllib2.URLError, e:
        return None


# create a row in our repo data object
def create_repo_data_object(repo):
    issue = repo.get('issue_events_url')
    commit = repo.get('commits_url')

    if (issue or commit) is None:
        return []
    else:
        issue_events_url = repo['issue_events_url'][0:len(repo['issue_events_url']) - 9],
        commits_url = repo['commits_url'][0:len(repo['commits_url']) - 6],

        entry = {
            "name": repo['name'],
            "language": repo['language'],
            "created_at": repo['created_at'],
            "url": repo['url'],
            "owner": repo['owner']['login'],
            "watch": repo['subscribers_count'],
            "forks": repo['forks_count'],
            "stars": repo['stargazers_count'],
            "issue_events_url": issue_events_url,
            "commits_url": commits_url,
            "time_line": fetch_time_line_data(commits_url, issue_events_url),
            "total_commits": repo_commits_count,
            "total_issues": repo_issues_count,
            "total_closed_issues": repo_closed_issues_count,
            "total_commits_comments": repo_commits_comments_count,
            "total_issues_comments": repo_issues_comments_count,
            "total_pos_commit_comments": commits_positive_comments_count,
            "total_neg_commit_comments": commits_negative_comments_count,
            "total_pos_issues_comments": issues_positive_comments_count,
            "total_neg_issues_comments": issues_negative_comments_count,
            "commits_pos_comments_prob_sum": commits_pos_comments_prob_sum,
            "commits_neg_comments_prob_sum": commits_neg_comments_prob_sum,
            "commits_neutral_comments_prob_sum": commits_neutral_comments_prob_sum,
            "issues_pos_comments_prob_sum": issues_pos_comments_prob_sum,
            "issues_neg_comments_prob_sum": issues_neg_comments_prob_sum,
            "issues_neutral_comments_prob_sum": issues_neutral_comments_prob_sum
        }

        pprint.pprint(entry)


# extract content from commits url
def fetch_time_line_data(commit_url, issue_url):
    try:
        # fetching from commits url
        page = 1
        data = fetch(add_url_query(commit_url, page), True)

        if data is None:
            return []
        extract_from_commit(data)

        while len(list(data)) == 100:
            page += 1
            data = fetch(add_url_query(commit_url, page), True)
            extract_from_commit(data)

        # fetching from issue url
        page = 1
        data = fetch(add_url_query(issue_url, page), True)
        if data is None:
            return []
        extract_from_issue(data)

        while len(list(data)) == 100:
            page += 1
            data = fetch(add_url_query(issue_url, page), True)
            extract_from_issue(data)

        return sorted(time_line_array, key=lambda i: i['created_at'])

    except Exception as e:
        return []


# extract necessary information from commits
def extract_from_commit(data):

    global repo_commits_count

    try:
        for commitObj in data:

            repo_commits_count += 1

            date = commitObj['commit']['author']['date']
            message = commitObj['commit']['message']
            url = commitObj['url']

            # Fetch some information from each individual commits urls
            data_from_commit_url = fetch(add_url_query(url, 1), True)

            comments_count = data_from_commit_url['commit']['comment_count']
            comments_url = data_from_commit_url['comments_url']

            comments = {}

            if comments_count > 0:
                comments = extract_from_comment(comments_url, comments_count, True)

            entry = {
                "commit_sha": commitObj['sha'],
                "url": url,
                "committer_name": commitObj['commit']['author']['name'],
                "created_at": date,
                "message": message,
                "isMergePR": True if "Merge pull request #" in message else False,
                "type": "Commit",
                # You apply commit comments directly to a commit and you apply issue comments without referencing a portion of the unified diff.
                "comments_count": comments_count,
                "comments_url": comments_url,
                "comments": comments,
                "addition": data_from_commit_url['stats']['additions'],
                "deletion": data_from_commit_url['stats']['deletions']
            }

            time_line_array.append(entry)

    except Exception as e:
        return []


# extract necessary information from issues
# Issues are the same as the PRs, They have the same created/closed dates, ... etc.
def extract_from_issue(data):

    global repo_issues_count, repo_closed_issues_count

    try:
        for issueObj in data:

            repo_issues_count += 1

            entry = {}
            issue_number = issueObj['issue']['number']

            # make sure to exclude the duplicate issues
            if issue_number not in issue_numbers_temp_array:

                issue_numbers_temp_array.append(issue_number)

                state = issueObj['issue']['state']
                pull_request_url = issueObj['issue']['pull_request']['url']

                # fetch the data from a pr url to extract the needed info
                data_from_pr_url = fetch(add_url_query(pull_request_url, 1), True)

                comments_count = issueObj['issue']['comments']
                comments_url = issueObj['issue']['comments_url']

                comments = {}

                if comments_count > 0:
                    comments = extract_from_comment(comments_url, comments_count, False)

                if state == 'closed':

                    repo_closed_issues_count += 1

                    entry_closed = {
                        "issue_number": issue_number,
                        # The time that the issue was closed at
                        # Called it created at just for sorting purposes
                        "created_at": issueObj['issue']['closed_at'],
                        "closed_by": issueObj['actor']['login'],
                        "type": "IssueClosed"
                    }

                    time_line_array.append(entry_closed)

                entry = {
                    "issue_number": issue_number,
                    "url": issueObj['issue']['url'],
                    "title": issueObj['issue']['title'],
                    "body": issueObj['issue']['body'],
                    "pull_request_url": pull_request_url,
                    "created_by": issueObj['issue']['user']['login'],
                    "created_at": issueObj['issue']['created_at'],
                    "isClosed": True if state == 'closed' else False,
                    "type": "IssueOpened",
                    # You apply commit comments directly to a commit and you apply issue comments without referencing a portion of the unified diff.
                    "comments_count": comments_count,
                    "comments_url": comments_url,
                    "comments": comments,
                    "addition": data_from_pr_url['additions'],
                    "deletion": data_from_pr_url['deletions'],
                    # Pull request review comments are comments on a portion of the unified diff made during a pull request review.
                    "review_comments_count": data_from_pr_url['review_comments'],
                    "review_comments_url": data_from_pr_url['review_comments_url']
                }

                time_line_array.append(entry)

    except Exception as e:
        return []


# Analyse a text to find its sentiment probabilities
def sentiment_prob(body, from_commit):

    global commits_positive_comments_count, commits_negative_comments_count, issues_positive_comments_count, issues_negative_comments_count
    global commits_pos_comments_prob_sum, commits_neg_comments_prob_sum, commits_neutral_comments_prob_sum
    global issues_pos_comments_prob_sum, issues_neg_comments_prob_sum, issues_neutral_comments_prob_sum

    text = urllib.urlencode({"text": body})
    st = urllib.urlopen("http://text-processing.com/api/sentiment/", text)

    returned_json = json.loads(st.read())

    positive_prob = returned_json['probability']['pos']
    neutral_prob = returned_json['probability']['neutral']
    negative_prob = returned_json['probability']['neg']
    label = returned_json['label']

    is_positive = 0
    is_negative = 0

    if 'pos' in label:
        is_positive += 1
    elif 'neg' in label:
        is_negative += 1

    if from_commit:
        commits_pos_comments_prob_sum += positive_prob
        commits_neg_comments_prob_sum += negative_prob
        commits_neutral_comments_prob_sum += neutral_prob

        commits_positive_comments_count += is_positive
        commits_negative_comments_count += is_negative
    else:
        issues_pos_comments_prob_sum += positive_prob
        issues_neg_comments_prob_sum += negative_prob
        issues_neutral_comments_prob_sum += neutral_prob

        issues_positive_comments_count += is_positive
        issues_negative_comments_count += is_negative

    return returned_json


# extract data from comments url
def extract_from_comment(url, comments_count, from_commit):

    global repo_commits_comments_count, repo_issues_comments_count

    data_from_comments = fetch(add_url_query(url, 1), True)
    entry = {}
    if len(data_from_comments) > 0:
        for comment in data_from_comments:
            body = comment['body']
            st_prob = sentiment_prob(body, from_commit)['probability']
            st_label = sentiment_prob(body, from_commit)['label']

            entry = {
                'url': comment['url'],
                'commenter': comment['user']['login'],
                'comment_created_at': comment['created_at'],
                'body': body,
                'positive': st_prob['pos'],
                'neutral': st_prob['neutral'],
                'negative': st_prob['neg'],
                'label': st_label
            }

    if from_commit:
        repo_commits_comments_count += comments_count
    else:
        repo_issues_comments_count += comments_count

    return entry


# convert date/time stamp to a regular string
def change_date_to_string(date):
    dt = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    return str(dt.year) + str(dt.month) + str(dt.day) + str(dt.hour) + str(dt.minute) + str(dt.second)


def time_elapsed():
    elapsed_time = time.time() - start
    return str(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))


# a small function to output which repo index is already done, how long it takes, and how many calls are remaining
def progress(i):
    print
    print '#' * 100
    print 'repository num  = ' + str(i)
    print 'limit remaining = ' + str(git_api_rate_limit())
    print 'api calls took  = ' + str(api_call)
    print 'time elapsed    = ' + time_elapsed()
    print '#' * 100
    print


# initialize the counters for each repo commit counts, issue counts, and sentiments analysis probabilities
def initialize_statistics_counters():
    global repo_commits_count, repo_issues_count, repo_closed_issues_count, repo_commits_comments_count, repo_issues_comments_count
    global commits_positive_comments_count, commits_negative_comments_count, issues_positive_comments_count, issues_negative_comments_count
    global commits_pos_comments_prob_sum, commits_neg_comments_prob_sum, commits_neutral_comments_prob_sum
    global issues_pos_comments_prob_sum, issues_neg_comments_prob_sum, issues_neutral_comments_prob_sum

    repo_commits_count = 0
    repo_issues_count = 0
    repo_closed_issues_count = 0
    repo_commits_comments_count = 0
    repo_issues_comments_count = 0
    commits_positive_comments_count = 0
    commits_negative_comments_count = 0
    issues_positive_comments_count = 0
    issues_negative_comments_count = 0
    commits_pos_comments_prob_sum = 0
    commits_neg_comments_prob_sum = 0
    commits_neutral_comments_prob_sum = 0
    issues_pos_comments_prob_sum = 0
    issues_neg_comments_prob_sum = 0
    issues_neutral_comments_prob_sum = 0


# The main function
if __name__ == "__main__":
    i = 0
    global start

    for e in repos.find():
        i += 1
        api_call = 0
        repo_commits_count = 0
        repo_issues_count = 0
        repo_closed_issues_count = 0
        repo_commits_comments_count = 0
        repo_issues_comments_count = 0
        commits_positive_comments_count = 0
        commits_negative_comments_count = 0
        issues_positive_comments_count = 0
        issues_negative_comments_count = 0
        commits_pos_comments_prob_sum = 0
        commits_neg_comments_prob_sum = 0
        commits_neutral_comments_prob_sum = 0
        issues_pos_comments_prob_sum = 0
        issues_neg_comments_prob_sum = 0
        issues_neutral_comments_prob_sum = 0

        # filter out the repos with no issues
        if (e['open_issues_count']) != 0:
            start = time.time()
            time_line_array = []
            issue_numbers_temp_array = []

            # initialize_statistics_counters()

            create_repo_data_object(e)
            progress(i)
            break


# add to issues (addition/deletion/comments url/ comments_count)
# document the difference between issue and pull request (Answer: They are the same)
# find the offset (index) of the repo I am currently on and return it
# find the time that is spent for one repo
# find the calls it took for a repo + the calls remaining for our 1 hour usage of github
# Fix the non length issue when fetch a url
# work around finding code reviews (isCodeReviewed) (isCommented) ---> code review can be recognized if comment_count > 0
# who is creating an issue and who is closing it
# very important: work around the sentiment analysis (if a comment was added)
# find whether the code is testable or not ---> No way to see this
# at the end, find the percentage of the commits / issues / prs that were code reviewed

########################################################################################################################

# look around releases / milestones to check other users' reviews about the product
# Think about creating a model that represents the current data model (repo time line)
# How can I improve the model?
# repo popularity (stars) evolution/history (in order to see if it's related to the code quality)
# Very last step, is to make sure you add each entry for each repo in a mongo db
