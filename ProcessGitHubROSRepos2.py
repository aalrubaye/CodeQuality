import json
import pprint
import time
import urllib2

from pymongo import MongoClient
import urllib
import Utility

__author__ = 'Abduljaleel Al Rubaye'

client = MongoClient()
database = client.github_data
repos = database.repos

time_line_db_array = [
    database.ros_repo_4250,
database.ros_repo_4257,
database.ros_repo_4258,
database.ros_repo_4259,
database.ros_repo_4260,
database.ros_repo_4261,
database.ros_repo_4262,
database.ros_repo_4263,
database.ros_repo_4264,
database.ros_repo_4265,
database.ros_repo_4266,
database.ros_repo_4267,
database.ros_repo_4268,
database.ros_repo_4269,
database.ros_repo_4270,
database.ros_repo_4271,
database.ros_repo_4272,
database.ros_repo_4273,
database.ros_repo_4274,
database.ros_repo_4275,
database.ros_repo_4276,
database.ros_repo_4277,
database.ros_repo_4278,
database.ros_repo_4279
]

uurl = [
 'https://api.github.com/repos/chainer/chainer',
 'https://api.github.com/repos/zihangdai/xlnet',
 'https://api.github.com/repos/dragen1860/TensorFlow-2.x-Tutorials',
 'https://api.github.com/repos/extreme-assistant/CVPR2020-Paper-Code-Interpretation',
 'https://api.github.com/repos/facebookresearch/wav2letter',
 'https://api.github.com/repos/wkentaro/labelme',
 'https://api.github.com/repos/tiny-dnn/tiny-dnn',
 'https://api.github.com/repos/PaddlePaddle/Paddle-Lite',
 'https://api.github.com/repos/microsoft/nlp-recipes',
 'https://api.github.com/repos/PaddlePaddle/models',
 'https://api.github.com/repos/aymericdamien/TopDeepLearning',
 'https://api.github.com/repos/h2oai/h2o-3',
 'https://api.github.com/repos/haifengl/smile',
 'https://api.github.com/repos/Ewenwan/MVision',
 'https://api.github.com/repos/transcranial/keras-js',
 'https://api.github.com/repos/NVIDIA/pix2pixHD',
 'https://api.github.com/repos/poloclub/cnn-explainer',
 'https://api.github.com/repos/tensorflow/serving',
 'https://api.github.com/repos/blei-lab/edward',
 'https://api.github.com/repos/stanfordnlp/stanza',
 'https://api.github.com/repos/deepmipt/DeepPavlov',
 'https://api.github.com/repos/wb14123/seq2seq-couplet',
 'https://api.github.com/repos/deepmind/graph_nets',
 'https://api.github.com/repos/astorfi/TensorFlow-World']

privateVar = open("privateVar2.txt", 'r').read()
client_id = privateVar.split('\n', 1)[0]
client_secret = privateVar.split('\n', 1)[1]

global issue_numbers_temp_array, api_call, start, author_list, do_print, sha_list, starting_apicall, repos_str
global repo_commits_count, repo_issues_count, repo_closed_issues_count, repo_issues_comments_count, time_line_db


# appends the client id and the client secret to urls
def add_url_query(url, page):
    query = '?per_page=100&page=' + str(page) + '&client_id=' + client_id + '&client_secret=' + client_secret
    if len(url) == 1:
        return url[0] + query
    else:
        return url + query


# fetch how many more calls we have for the hour
def git_api_rate_limit():
    url = add_url_query("https://api.github.com/rate_limit", 1)
    try:
        json_url = urllib.urlopen(url)
        data = json.loads(json_url.read())

        return data['rate']['remaining']
    except Exception as er:
        Utility.show_progress_message(do_print, 'Error on Fetch Function: (' + str(er.message) + ')')
        return 0


# Wait function wo make sure we are not exceeding the github API limit
def pause_if_limit_exceeded():
    global api_call

    while api_call < 50:
        print 'The rate limit exceeded. Please wait...'
        api_call = git_api_rate_limit()
        time.sleep(60)


# Returns data from a call to a url
def fetch(url, count_call):
    global api_call
    pause_if_limit_exceeded()
    try:
        json_url = urllib.urlopen(url)
        time.sleep(0.5)
        data = json.loads(json_url.read())
        if count_call:
            api_call -= 1
        return data
    except Exception as er:
        Utility.show_progress_message(do_print, 'Error on Fetch Function: (' + str(er.message) + ')')
        return None


# initialize the counters for each repo commit counts, issue counts, and sentiments analysis probabilities
def initialize_statistics_counters():
    global repo_commits_count, repo_issues_count, repo_closed_issues_count, repo_issues_comments_count

    repo_commits_count = 0
    repo_issues_count = 0
    repo_closed_issues_count = 0
    repo_issues_comments_count = 0


# return the number of repos contributors
def fetch_repo_contributors_count(url):
    try:
        count = 0
        page = 1
        data = fetch(add_url_query(url, page), True)
        while len(list(data)) == 100:
            Utility.show_progress_message(do_print, 'Fetching repo contributors...'+str(page))

            count += 100
            page += 1
            data = fetch(add_url_query(url, page), True)

        count += len(list(data))
        return count

    except Exception as er:
        Utility.show_progress_message(do_print, 'Error on Fetching Contributors Count: (' + str(er.message) + ')')
        return 0


# fetch num of committer's followers
def fetch_authors_followers_count(author, url):

    search_author = next((item for item in author_list if item["author"] == author), False)
    if search_author is False:
        try:
            Utility.show_progress_message(do_print, 'Fetching author followers for: ' + author + '...')
            data = fetch(add_url_query(url, 1), True)

            count = data['followers']
            entry = {
                        'author': author,
                        'followers': count
                    }
            author_list.append(entry)
            return count

        except Exception as er:
            Utility.show_progress_message(do_print, 'Error on Authors Count Function: (' + str(er.message) + ')')
            return 0
    else:
        return search_author['followers']


# extract content from commits url
def fetch_time_line_data(commit_url, issue_url):
    try:
        # fetching from issue url
        page = 1
        issues_data = fetch(add_url_query(issue_url, page), True)
        if issues_data is not None:
            extract_from_issue(issues_data)

        while len(list(issues_data)) == 100:
            page += 1
            issues_data = fetch(add_url_query(issue_url, page), True)
            extract_from_issue(issues_data)

        if repo_issues_count == 0:
            return []

        # fetching from commits url
        page = 1
        commits_data = fetch(add_url_query(commit_url, page), True)
        if commits_data is not None:
            extract_from_commit(commits_data)

        while len(list(commits_data)) == 100:
            page += 1
            commits_data = fetch(add_url_query(commit_url, page), True)
            extract_from_commit(commits_data)


        return

    except Exception as er:
        Utility.show_progress_message(do_print, 'Error on TimeLine Function: (' + str(er.message) + ')')
        return []


# extract necessary information from commits
def extract_from_commit(data):

    global repo_commits_count, sha_list, time_line_db
    try:
        for commitObj in data:
            message = commitObj['commit']['message']
            sha = commitObj['sha']
            if "Merge pull request #" not in message:
                if sha not in sha_list:
                    repo_commits_count += 1
                    sha_list.append(sha)

                    date = commitObj['commit']['author']['date']
                    url = commitObj['url']

                    author = commitObj.get('author')
                    if author:
                        author = commitObj.get('author').get('login')
                        author_url = commitObj.get('author').get('url')

                        author_followers_count = fetch_authors_followers_count(author, author_url)

                        Utility.show_progress_message(do_print, 'Commit from: ' + str(author) + '...')

                        entry = {
                            "sha": sha,
                            "url": url,
                            "author": author,
                            "author_followers_count": author_followers_count,
                            "created_at": date,
                            "message": message,
                            "type": "Commit",
                            "issue_number": None
                        }

                        time_line_db.insert(entry)
        return

    except Exception as er:
        Utility.show_progress_message(do_print, 'Error on Commits Function: (' + str(er.message) + ')')
        return []


# extract necessary information from issues
# Issues are the same as the PRs, They have the same created/closed dates, ... etc.
def extract_from_issue(data):

    global repo_issues_count, repo_closed_issues_count, time_line_db
    try:
        for issueObj in data:
            issue_number = issueObj['issue']['number']

            # ensure to exclude the duplicate issues
            if issue_number not in issue_numbers_temp_array:

                issue_numbers_temp_array.append(issue_number)

                state = issueObj['issue']['state']
                author = issueObj['issue']['user']['login']
                Utility.show_progress_message(do_print, 'Issue from: ' + str(author) + '...')
                author_url = issueObj['issue']['user']['url']
                author_followers_count = fetch_authors_followers_count(author, author_url)
                comments_count = issueObj['issue']['comments']
                comments_url = issueObj['issue']['comments_url']
                comments = {}
                seconds_to_closed = None

                if state == 'closed':
                    if issueObj.get('actor'):
                        repo_closed_issues_count += 1
                        closed_by = issueObj['actor']['login']

                        if closed_by == author:
                            close_author_followers_count = author_followers_count
                        else:
                            close_author_url = issueObj['actor']['url']
                            close_author_followers_count = fetch_authors_followers_count(closed_by, close_author_url)

                        seconds_to_closed = Utility.time_diff(issueObj['issue']['closed_at'], issueObj['issue']['created_at'])
                        entry_closed = {
                            "issue_number": issue_number,
                            "created_at": issueObj['issue']['closed_at'],
                            "author": closed_by,
                            "author_followers_count": close_author_followers_count,
                            "type": "IssueClosed",
                            "seconds_to_close": seconds_to_closed
                        }
                        time_line_db.insert(entry_closed)

                if comments_count > 0:
                    extract_from_comment(comments_url, issue_number)

                pull_request_url = None
                commits_count = 0
                addition = 0
                deletion = 0
                review_comments_count = 0
                review_comments_url = None

                pr = issueObj.get('issue').get('pull_request')
                if pr:
                    pull_request_url = issueObj['issue']['pull_request']['url']
                    pull_request_commits = pull_request_url+'/commits'

                    # fetch the data from a pr url to extract the needed info
                    data_from_pr_url = fetch(add_url_query(pull_request_url, 1), True)

                    if len(data_from_pr_url) > 0:
                        commits_count = data_from_pr_url.get('commits')
                        addition = data_from_pr_url.get('additions')
                        deletion = data_from_pr_url.get('deletions')
                        # Pull request review comments are comments on a portion of the unified diff made during a pull request review.
                        review_comments_count = data_from_pr_url.get('review_comments')
                        review_comments_url = data_from_pr_url.get('review_comments_url')

                        fetch_issue_pr_commit(issue_number, pull_request_commits, author, author_followers_count)

                repo_issues_count += 1
                entry = {
                    "issue_number": issue_number,
                    "url": issueObj['issue']['url'],
                    "title": issueObj['issue']['title'],
                    "body": issueObj['issue']['body'],
                    "pull_request_url": pull_request_url,
                    "author": author,
                    "author_followers_count": author_followers_count,
                    "created_at": issueObj['issue']['created_at'],
                    "isClosed": True if state == 'closed' else False,
                    "seconds_to_close": seconds_to_closed,
                    "type": "IssueOpened",
                    "commits_count": commits_count,
                    # You apply commit comments directly to a commit and you apply issue comments without referencing a portion of the unified diff.
                    "comments_count": comments_count,
                    "comments_url": comments_url,
                    "addition": addition,
                    "deletion": deletion,
                    # Pull request review comments are comments on a portion of the unified diff made during a pull request review.
                    "review_comments_count": review_comments_count,
                    "review_comments_url": review_comments_url
                }

                time_line_db.insert(entry)

        return

    except Exception as er:
        Utility.show_progress_message(do_print, 'Error on Issues Function: (' + str(er.message) + ')')
        return []


# extract the commit that comes right before the open issue from the open issue's pr url
def fetch_issue_pr_commit(issue_number, url, pr_author, pr_author_followers_count):
    global repo_commits_count, sha_list, time_line_db
    try:

        commits_data = fetch(add_url_query(url, 1), True)

        for cmt in commits_data:

            message = cmt['commit']['message']
            sha = cmt['sha']

            # we don't want to include commits coming automatically after the pr merge
            # these kind of commits are automatically generated by gitHub
            # the event of closing a pr is tracked by (issueClosed) data object
            # if "Merge pull request #" not in message:
            if sha not in sha_list:
                repo_commits_count += 1
                sha_list.append(sha)

            author = cmt['author']
            if author is None:
                author_id = pr_author
                author_followers_count = pr_author_followers_count
            else:
                author_id = cmt['author']['login']
                author_url = cmt['author']['url']

                author_followers_count = fetch_authors_followers_count(author_id, author_url)

            Utility.show_progress_message(do_print, 'Issue Commits from: ' + str(author_id) + '...')
            entry = {
                "sha": sha,
                "url": cmt['url'],
                "author": author_id,
                "author_followers_count": author_followers_count,
                "created_at": cmt['commit']['author']['date'],
                "message": message,
                "type": "Commit",
                "issue_number": issue_number
            }
            time_line_db.insert(entry)
        return
    except Exception as er:
        Utility.show_progress_message(do_print, 'Error on Pre open Issue Commits: (' + str(er.message) + ')')
        return


# extract data from comments url
def extract_from_comment(url, issue_number):

    global repo_issues_comments_count, time_line_db
    try:

        data_from_comments = fetch(add_url_query(url, 1), True)

        if len(data_from_comments) > 0:
            for comment in data_from_comments:
                body = comment['body']
                sentiment = Utility.sentiment_score(body)
                sentiment_score = sentiment['score']
                sentiment_label = sentiment['label']

                author = comment['user']['login']
                author_url = comment['user']['url']
                author_followers_count = fetch_authors_followers_count(author, author_url)
                Utility.show_progress_message(do_print, 'Comment from: ' + str(author) + '...')
                entry = {
                    'url': comment['url'],
                    'author': author,
                    "issue_number": issue_number,
                    "author_followers_count": author_followers_count,
                    'comment_created_at': comment['created_at'],
                    'body': body,
                    'sentiment_score': sentiment_score,
                    'sentient_label': sentiment_label,
                    "type": "Comment"
                }
                repo_issues_comments_count += 1
                time_line_db.insert(entry)

        return
    except Exception as er:
        Utility.show_progress_message(do_print, 'Error on comments: (' + str(er.message) + ')')
        return {}


# Returns data from a call to a url
def fetch2(url):

    global api_call
    pause_if_limit_exceeded()

    try:
        # print url
        req = urllib2.Request(url)
        req.add_header("Accept","application/vnd.github.mercy-preview+json")
        resp = urllib2.urlopen(req)
        # data = json.loads(json_url.read())
        data = json.loads(resp.read())
        # api_call -= 1
        return data

    except Exception as er:
        print 'Error on Fetch2 Function: (' + str(er.message) + ')'
        return None


def fetch_repo_topic_list(repo_url):
    try:
        data = fetch2(add_url_query(repo_url+'/topics', 1))
        return data

    except Exception as er:
        print er.message


# create a row in our repo data object
def create_repo_data_object(repo_url):
    global time_line_db
    repo = fetch(add_url_query(repo_url, 1), True)
    if repo.get('id'):
        issue_events_url = repo_url+'/issues/events'
        commits_url = repo_url +'/commits'
        owner = repo['owner']['login']
        owner_url = repo['owner']['url']
        owner_followers_count = fetch_authors_followers_count(owner, owner_url)
        repo_contributors_url = repo['contributors_url']
        repo_contributors_count = fetch_repo_contributors_count(repo_contributors_url)
        fetch_time_line_data(commits_url, issue_events_url)
        topics = fetch_repo_topic_list(repo_url)

        entry = {
            "name": repo['name'],
            "language": repo['language'],
            "owner": repo['owner']['login'],
            "owner_followers_count": owner_followers_count,
            "contributors_count": repo_contributors_count,
            "created_at": repo['created_at'],
            "urls": {
                "repo_url": repo['url'],
                "issue_events_url": issue_events_url,
                "commits_url": commits_url
            },
            "popularity": {
                "watch": repo['subscribers_count'],
                "forks": repo['forks_count'],
                "stars": repo['stargazers_count']
            },
            "statistics": {
                "total_commits": repo_commits_count+1,
                "total_issues": repo_issues_count,
                "total_closed_issues": repo_closed_issues_count,
                "total_issues_comments": repo_issues_comments_count
            },
            "topics": topics
        }

        time_line_db.insert(entry)


# a small function to output which repo index is already done, how long it takes, and how many calls are remaining
def progress():
    print
    print '#' * 100
    print 'limit remaining = ' + str(api_call)
    print 'api calls took  = ' + str(starting_apicall - api_call)
    print 'time elapsed    = ' + Utility.time_elapsed(start)
    print '#' * 100
    print


# The main function
if __name__ == "__main__":
    global start, author_list, do_print, starting_apicall, time_line_db

    # print time_line_db.count()
    # pprint.pprint(time_line_db.find()[time_line_db.count()-1])

    for r in range (0, len(time_line_db_array)):

        do_print = True

        try:
            api_call = git_api_rate_limit()
            starting_apicall = api_call

            start = time.time()
            author_list = []
            sha_list = []
            issue_numbers_temp_array = []
            time_line_db = time_line_db_array[r]

            initialize_statistics_counters()
            create_repo_data_object(uurl[r])

        except Exception as er:
                Utility.show_progress_message(do_print, 'Error on fetching repos: (' + str(er.message) + ')')
