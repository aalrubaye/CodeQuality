import json
import pprint
import time
from pymongo import MongoClient
import urllib
import Utility
import sklearn

__author__ = 'Abdul Rubaye'

client = MongoClient()
database = client.github_data
repos = database.repos
pull_requests = database.pull_requests
events = database.events
commits = database.commits.bson
commit_comments = database.commit_comments

time_line_db = database.time_line

global time_line_array, issue_numbers_temp_array, api_call, start, author_list, do_print, sha_list, starting_apicall, repos_str
global repo_commits_count, repo_issues_count, repo_closed_issues_count, repo_commits_comments_count, repo_issues_comments_count
global commits_positive_comments_count, commits_negative_comments_count, issues_positive_comments_count, issues_negative_comments_count
global commits_pos_comments_prob_sum, commits_neg_comments_prob_sum, commits_neutral_comments_prob_sum
global issues_pos_comments_prob_sum, issues_neg_comments_prob_sum, issues_neutral_comments_prob_sum

# client id and client secret are used in calling the github API
# they will help to raise the maximum limit of calls per hour
# note: you will need your private txt file that includes the private keys
privateVar = open("privateVar.txt", 'r').read()
# privateVar = open("privateVar2.txt", 'r').read()
client_id = privateVar.split('\n', 1)[0]
client_secret = privateVar.split('\n', 1)[1]


# fetch how many more calls we have for the hour
def git_api_rate_limit():
    url = add_url_query("https://api.github.com/rate_limit", 1)
    try:
        json_url = urllib.urlopen(url)
        data = json.loads(json_url.read())

        return data['rate']['remaining']
    except urllib.URLError, e:
        Utility.show_progress_message(do_print, 'Error on Fetch Function: (' + str(e.message) + ')')
        return 0


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
    pause_if_limit_exceeded()
    try:

        json_url = urllib.urlopen(url)
        data = json.loads(json_url.read())

        if count_call:
            api_call -= 1
        return data
    except urllib2.URLError, e:
        Utility.show_progress_message(do_print, 'Error on Fetch Function: (' + str(e.message) + ')')
        return None


# Wait function wo make sure we are not exceeding the github API limit
def pause_if_limit_exceeded():
    global api_call

    while api_call < 50:
        print 'The rate limit exceeded. Please wait...'
        repo_names_write = open("reponames.txt", 'w')
        repo_names_write.write(repos_str)
        repo_names_write.close()
        api_call = git_api_rate_limit()
        time.sleep(120)


# Some of the recorded repos are removed from GitHub, so we need to filter
def verify_repo_still_exists(repo):

    try:
        url = repo['url']
        data = fetch(add_url_query(url, 1), True)
        if data.get('id'):
            return True
        else:
            return False
    except Exception as e:
        Utility.show_progress_message(do_print, 'The repo does not exist anymore: (' + str(e.message) + ')')
        return False


# create a row in our repo data object
def create_repo_data_object(repo):
    verify_repo_still_exists(repo)

    if verify_repo_still_exists(repo) is False:
        return []
    else:
        # issue = repo.get('issue_events_url')
        # commit = repo.get('commits_url')
        issue_events_url = repo['issue_events_url'][0:len(repo['issue_events_url']) - 9]
        commits_url = repo['commits_url'][0:len(repo['commits_url']) - 6]
        owner = repo['owner']['login']
        owner_url = repo['owner']['url']

        owner_followers_count = fetch_authors_followers_count(owner, owner_url)
        repo_contributors_url = repo['contributors_url']
        repo_contributors_count = fetch_repo_contributors_count(repo_contributors_url)
        time_line_entries = fetch_time_line_data(commits_url, issue_events_url)

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
            "time_line": time_line_entries,
            "statistics": {
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
        }

        # if len(time_line_entries) > 0:
        #     time_line_db.insert(entry)


# return the number of repos contributors
def fetch_repo_contributors_count(url):
    try:
        count = 0
        page = 1
        data = fetch(add_url_query(url, page), True)
        Utility.show_progress_message(do_print, 'Fetching repo contributors...')
        while len(list(data)) == 100:
            count += 100
            page += 1
            data = fetch(add_url_query(url, page), True)

        count += len(list(data))
        return count

    except Exception as e:
        Utility.show_progress_message(do_print, 'Error on Fetching Contributors Count: (' + str(e.message) + ')')
        return 0


# Fetch num of committer's followers
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

        except Exception as e:
            Utility.show_progress_message(do_print, 'Error on Authors Count Function: (' + str(e.message) + ')')
            return 0
    else:
        return search_author['followers']


# extract content from commits url
def fetch_time_line_data(commit_url, issue_url):
    try:
        # fetching from issue url
        page = 1
        data = fetch(add_url_query(issue_url, page), True)
        if data is not None:
            extract_from_issue(data)

        while len(list(data)) == 100:
            page += 1
            data = fetch(add_url_query(issue_url, page), True)
            extract_from_issue(data)

        if repo_issues_count == 0:
            return []

        # fetching from commits url
        page = 1
        data = fetch(add_url_query(commit_url, page), True)

        if data is not None:
            extract_from_commit(data)

        while len(list(data)) == 100:
            page += 1
            data = fetch(add_url_query(commit_url, page), True)
            extract_from_commit(data)

        sorted_time_line = sorted(time_line_array, key=lambda i: i['created_at'])
        # Utility.export_time_line_data(sorted_time_line)

        return sorted_time_line

    except Exception as e:
        Utility.show_progress_message(do_print, 'Error on TimeLine Function: (' + str(e.message) + ')')
        return []


# extract necessary information from commits
def extract_from_commit(data):

    global repo_commits_count, sha_list
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
                author = commitObj['author']['login']
                author_url = commitObj['author']['url']

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

                time_line_array.append(entry)

    except Exception as e:
        Utility.show_progress_message(do_print, 'Error on Commits Function: (' + str(e.message) + ')')
        return []


# extract necessary information from issues
# Issues are the same as the PRs, They have the same created/closed dates, ... etc.
def extract_from_issue(data):

    global repo_issues_count, repo_closed_issues_count

    try:
        for issueObj in data:
            issue_number = issueObj['issue']['number']

            # ensure to exclude the duplicate issues
            if issue_number not in issue_numbers_temp_array:
                issue_numbers_temp_array.append(issue_number)
                pprint.pprint(issueObj)
                state = issueObj['issue']['state']
                pr = issueObj.get('issue').get('pull_request')

                if pr:
                    pull_request_url = issueObj['issue']['pull_request']['url']
                    pull_request_commits = pull_request_url+'/commits'

                    # fetch the data from a pr url to extract the needed info
                    data_from_pr_url = fetch(add_url_query(pull_request_url, 1), True)

                    author = issueObj['issue']['user']['login']
                    author_url = issueObj['issue']['user']['url']

                    author_followers_count = fetch_authors_followers_count(author, author_url)

                    Utility.show_progress_message(do_print, 'Issue from: ' + str(author) + '...')

                    comments_count = issueObj['issue']['comments']
                    comments_url = issueObj['issue']['comments_url']
                    comments = {}
                    print ('here1')
                    seconds_to_closed = None
                    if comments_count > 0:
                        print ('here22')
                        print comments_url
                        comments = extract_from_comment(comments_url, comments_count, False)

                    if state == 'closed':
                        repo_closed_issues_count += 1
                        closed_by = issueObj['actor']['login']

                        if closed_by == author:
                            close_author_followers_count = author_followers_count
                        else:
                            close_author_url = issueObj['actor']['url']
                            close_author_followers_count = fetch_authors_followers_count(closed_by, close_author_url)

                        seconds_to_closed = Utility.time_diff(issueObj['issue']['closed_at'], issueObj['issue']['created_at'])
                        print ('here2')
                        entry_closed = {
                            "issue_number": issue_number,
                            "created_at": issueObj['issue']['closed_at'],
                            "author": closed_by,
                            "author_followers_count": close_author_followers_count,
                            "type": "IssueClosed",
                            "seconds_to_close": seconds_to_closed
                        }

                        time_line_array.append(entry_closed)
                    print ('here3')
                    fetch_issue_pr_commit(issue_number, pull_request_commits, author, author_followers_count)
                    print ('here4')
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
                        "commits_count": data_from_pr_url['commits'],
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

                    # time_line_array.append(entry)

    except Exception as e:
        Utility.show_progress_message(do_print, 'Error on Issues Function: (' + str(e.message) + ')')
        return []


# extract the commit that comes right before the open issue from the open issue's pr url
def fetch_issue_pr_commit(issue_number, url, pr_author, pr_author_followers_count):
    global repo_commits_count, sha_list
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

            # time_line_array.append(entry)

    except Exception as e:
        Utility.show_progress_message(do_print, 'Error on Pre open Issue Commits: (' + str(e.message) + ')')
        return {}


# extract data from comments url
def extract_from_comment(url, comments_count, from_commit):

    global repo_commits_comments_count, repo_issues_comments_count
    print ('here 33')
    data_from_comments = fetch(add_url_query(url, 1), True)
    print ('here 44')
    entry = {}
    if len(data_from_comments) > 0:
        print ('here 55')
        for comment in data_from_comments:
            print ('here 66')
            body = comment['body']
            print body
            st_prob = sentiment_prob(body, from_commit)['probability']
            print st_prob
            st_label = sentiment_prob(body, from_commit)['label']
            print st_label
            author = comment['user']['login']
            print author
            author_url = comment['user']['url']
            print author_url
            print ('here 77')
            author_followers_count = fetch_authors_followers_count(author, author_url)
            print ('here 88')
            Utility.show_progress_message(do_print, 'Comment from: ' + str(author) + '...')
            print ('here 99')
            entry = {
                'url': comment['url'],
                'author': author,
                "author_followers_count": author_followers_count,
                'comment_created_at': comment['created_at'],
                'body': body,
                'positive': st_prob['pos'],
                'neutral': st_prob['neutral'],
                'negative': st_prob['neg'],
                'label': st_label,
                "type": "Comment"
            }

    if from_commit:
        repo_commits_comments_count += comments_count
    else:
        repo_issues_comments_count += comments_count

    return entry


# Analyse a text to find its sentiment probabilities
def sentiment_prob(body, from_commit):

    global commits_positive_comments_count, commits_negative_comments_count, issues_positive_comments_count, issues_negative_comments_count
    global commits_pos_comments_prob_sum, commits_neg_comments_prob_sum, commits_neutral_comments_prob_sum
    global issues_pos_comments_prob_sum, issues_neg_comments_prob_sum, issues_neutral_comments_prob_sum
    print 'hello'
    text = urllib.urlencode({"text": body})
    print 'hello222'
    st = urllib.urlopen("http://text-processing.com/api/sentiment/", text)
    print 'hello43434'
    print st.read()
    returned_json = json.loads(st.read())
    print 'hello34344'
    positive_prob = returned_json['probability']['pos']
    print 'hello111'
    neutral_prob = returned_json['probability']['neutral']
    print 'hello2'
    negative_prob = returned_json['probability']['neg']
    print 'hello3'
    label = returned_json['label']
    print 'hello4'

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


# a small function to output which repo index is already done, how long it takes, and how many calls are remaining
def progress(repo_num):
    print
    print '#' * 100
    print 'repository num  = ' + str(repo_num)
    print 'limit remaining = ' + str(api_call)
    print 'api calls took  = ' + str(starting_apicall - api_call)
    print 'time elapsed    = ' + Utility.time_elapsed(start)
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

    global start, author_list, do_print, starting_apicall
    do_print = True

    offset = 7858
    offset_end = 7859
    i = offset
    # repos.count() = 78222

    repo_names = open("reponames.txt", 'r')
    repos_str = repo_names.read()
    repo_names.close()

    for e in repos.find()[offset:offset_end]:

        repo_commits_count = 0; repo_issues_count = 0; repo_closed_issues_count = 0; repo_commits_comments_count = 0
        repo_issues_comments_count = 0; commits_positive_comments_count = 0; commits_negative_comments_count = 0
        issues_positive_comments_count = 0; issues_negative_comments_count = 0; commits_pos_comments_prob_sum = 0
        commits_neg_comments_prob_sum = 0; commits_neutral_comments_prob_sum = 0; issues_pos_comments_prob_sum = 0
        issues_neg_comments_prob_sum = 0; issues_neutral_comments_prob_sum = 0

        # ensure that we are not checking duplicate repos
        if e['name']+',' not in repos_str:
            repos_str += e['name'] + ','

            if e['open_issues_count'] > 0:
                api_call = git_api_rate_limit()
                starting_apicall = api_call

                print '-' * 100
                print 'repo number (' + str(i) + ') is in progress'
                print '-' * 100

                start = time.time()
                time_line_array = []
                author_list = []
                sha_list = []
                issue_numbers_temp_array = []

                initialize_statistics_counters()

                create_repo_data_object(e)
                progress(i)
        i += 1

    repo_names_write = open("reponames.txt", 'w')
    repo_names_write.write(repos_str)
    repo_names_write.close()
    #
    # print time_line_db.count()
    # for ii in time_line_db.find():
    #     print ii['statistics']['total_issues']




########################################################################################################################
# TODO Done

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
# function to show or hide certain "prints"
# function to show time elapsed while running each repo
# sort functions (try to find a way to use utility class for utility functions)
# commenter and committer details
# look around releases / milestones to check other users' reviews about the product
# document the data model for commit, issues, and comment
# review comments should be included (Answer: Not really, we can the url instead if any review available)
# Really Really important: I feel some commits are missing -> found it (it's pre open issue commits)
# include pre open issue commits
# include message/body/title in the spreadsheet
# include the time took for an issue to be closed (preferably in issue closed)
# define a def to export the time-line and the type of the event for each repo
# associate number of commits for each issue
# add comments to the commits in the def fetch_issue_pr_commit  -> not needed anymore
# Associate issue number with each commit
# Fix fetching commits for each PR
# sketch how they are laid down on the repo's time line (Does it make sense to use Gephi?)
# update the data model
# get rid of the repeated commits (Merge commits + repeated sha's)
# Repeated Commits should count as 1
# Define commit, comment, and Issue then talk about issueOpen, issueClose and their different
# repo contributor list/count
# repo owner followers count
# write down all possible statistic work that I can think of here (document the statistics as well)
# Raise questions about everything
# What is code quality? what can affect code quality? how to measure code quality?
# sample run to check potential errors (10 repos)
# add back pr review to issue data model -> Not needed
# Think about creating a model that represents the current data model (repo time line)
# How can I improve the model? Answers are is the doc
# now sketch one more time (Cannot do this now)
# repo popularity (stars) evolution/history (in order to see if it's related to the code quality) -> Don't need it now
# timer for Github API calls to not exceed the limit
# make sure to use multiple threads via using different Github API accounts to get more data within less time
# Make sure you add each entry for each repo in a MongoDB


########################################################################################################################
# TODO In progress:


########################################################################################################################
# TODO

# research about ML's prediction models to find one suitable for this work (https://www.youtube.com/watch?v=Ogh_lxM58rw)
            # important to watch: https://www.youtube.com/watch?v=JU9saQ8D8is
    # If you are trying to predict a continuous target, then you will need a regression model.
    # But if you are trying to predict a discrete target, then you will need a classification model.
    # https://towardsdatascience.com/the-beginners-guide-to-selecting-machine-learning-predictive-models-in-python-f2eb594e4ddc
    # https://machinelearningmastery.com/make-predictions-scikit-learn/
# Think of a data set to train in a ML model
# our approach to measure code quality
# How can we make the code more efficient related to its number of calls to Github API
# setup an overleaf initial paper



    # Utility.export_time_line_data([], 'pr35')
    # print Utility.change_date_to_string('2016-04-27T18:30:27Z')

#*********************************************************************
    # Findings:
    # Issue open = Pull request
    # issue open is a commit
    # issue close is a commit that merges a pull request
#*********************************************************************
