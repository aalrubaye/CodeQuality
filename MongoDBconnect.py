import pprint
import urllib2
from datetime import datetime
import simplejson
from pymongo import MongoClient

__author__ = 'Abdul Rubaye'

client = MongoClient()
database = client.github_data
repos = database.repos
pull_requests = database.pull_requests
events = database.events
commits = database.commits.bson
commit_comments = database.commit_comments
global time_line_array, issue_numbers_temp_array

# client id and client secret are used in calling the github API
# they will help to raise the maximum limit of calls per hour
# note: you will need your private txt file that includes the private keys
privateVar = open("privateVar.txt",'r').read()
client_id = privateVar.split('\n', 1)[0]
client_secret = privateVar.split('\n', 1)[1]


# fetch how many more calls we have for the hour
def git_api_rate_limit():
    data = fetch(add_url_query("https://api.github.com/rate_limit", 1))
    return data['rate']['remaining']


# appends the client id and the client secret to urls
def add_url_query (url, page):
    query = '?per_page=100&page='+str(page)+'&client_id='+client_id+'&client_secret='+client_secret
    if len(url) == 1:
        return url[0]+query
    else:
        return url+query


# Returns data from a call to a url
def fetch(url):
    try:
        request = urllib2.Request(url, headers={"Accept": "application/vnd.github.v3.star+json"})
        response = urllib2.urlopen(request)
        data = simplejson.load(response)
        return data
    except urllib2.URLError, e:
        return e


# create a row in our repo data object
def create_repo_data_object(repo):
    issue_events_url = repo['issue_events_url'][0:len(repo['issue_events_url'])-9],
    commits_url = repo['commits_url'][0:len(repo['commits_url'])-6],

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
        "time_line": fetch_time_line_data(commits_url,issue_events_url)
    }

    # pprint.pprint(entry)


# extract content from commits url
def fetch_time_line_data(commit_url,issue_url):
    # fetching from commits url
    page = 1
    data = fetch(add_url_query(commit_url, page))
    extract_from_commit(data)

    while len(data) == 100:
        page += 1
        data = fetch(add_url_query(commit_url, page))
        extract_from_commit(data)

    # fetching from issue url
    page = 1
    data = fetch(add_url_query(issue_url, page))
    extract_from_issue(data)

    while len(data) == 100:
        page += 1
        data = fetch(add_url_query(issue_url, page))
        extract_from_issue(data)

    return sorted(time_line_array, key=lambda i: i['created_at'])


# extract necessary information from commits
def extract_from_commit(data):

    for commitObj in data:
        date = commitObj['commit']['author']['date']
        message = commitObj['commit']['message']
        url = commitObj['url']

        data_from_commit_url = fetch(add_url_query(url, 1))

        entry = {
            "commit_sha": commitObj['sha'],
            "url": url,
            "committer_name": commitObj['commit']['author']['name'],
            "created_at": date,
            "message": message,
            "isMergePR": True if "Merge pull request #" in message else False,
            "type": "Commit",
            "comments_count": data_from_commit_url['commit']['comment_count'],
            "comments_url": data_from_commit_url['comments_url'],
            "addition": data_from_commit_url['stats']['additions'],
            "deletion": data_from_commit_url['stats']['deletions']
        }

        if data_from_commit_url['commit']['comment_count'] > 0:
            print '8888888888888888888888888888888888'
        time_line_array.append(entry)


# extract necessary information from issues
def extract_from_issue(data):

    for issueObj in data:
        entry = {}
        issue_number = issueObj['issue']['number']

        # make sure to exclude the duplicate issues
        if issue_number not in issue_numbers_temp_array:
            issue_numbers_temp_array.append(issue_number)

            url = issueObj['issue']['url']
            title = issueObj['issue']['title']
            comments_url = issueObj['issue']['comments_url']
            pull_request_url = issueObj['issue']['pull_request']['url']
            created_by = issueObj['issue']['user']['login']
            created_at = issueObj['issue']['created_at']
            state = issueObj['issue']['state']
            closed_at = issueObj['issue']['closed_at'] if 'closed' in state else None
            closed_by = None if closed_at is None else issueObj['actor']['login']

            if state == 'closed':
                entry_closed = {
                    "issue_number": issue_number,
                    "url": url,
                    "created_at": closed_at,
                    "closed_by": closed_by,
                    "type": "IssueClosed"
                }

                time_line_array.append(entry_closed)

            entry = {
                "issue_number": issue_number,
                "url": url,
                "title": title,
                "comments_url": comments_url,
                "pull_request_url": pull_request_url,
                "created_by": created_by,
                "created_at": created_at,
                "isClosed": True if state == 'closed' else False,
                "type": "IssueOpened"
            }

            time_line_array.append(entry)


# convert date/time stamp to a regular string
def change_date_to_string(date):
    dt = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    return str(dt.year)+str(dt.month)+str(dt.day)+str(dt.hour)+str(dt.minute)+str(dt.second)


# The main function
if __name__ == "__main__":
    i = 1
    for e in repos.find():
        # filter out the repos with no issues
        if (e['open_issues_count']) != 0:
            time_line_array = []
            issue_numbers_temp_array = []
            create_repo_data_object(e)
            break


#add to issues (addition/deletion/comments url/ comments_count)
