import json
import pprint
import time
import urllib
import urllib2

__author__ = 'Abduljaleel Al Rubaye'

global api_call

privateVar = open("privateVar.txt", 'r').read()
client_id = privateVar.split('\n', 1)[0]
client_secret = privateVar.split('\n', 1)[1]


# fetch how many more calls we have for the hour
def git_api_rate_limit():
    url = add_url_query("https://api.github.com/rate_limit", 1, True)
    try:
        json_url = urllib.urlopen(url)
        rate = json.loads(json_url.read())
        return rate['rate']['remaining']

    except Exception as er:
        print er.message
        return 0


# appends the client id and the client secret to urls
def add_url_query(url, page, is_rate):

    if is_rate:
        query = '?per_page=100&page=' + str(page) + '&client_id=' + client_id + '&client_secret=' + client_secret
    else:
        query = '&per_page=100&page=' + str(page) + '&client_id=' + client_id + '&client_secret=' + client_secret
    if len(url) == 1:

        return url[0] + query
    else:
        return url + query



# Wait function wo make sure we are not exceeding the github API limit
def pause_if_limit_exceeded():
    global api_call

    while api_call < 50:
        print 'The rate limit exceeded. Please wait...'
        api_call = git_api_rate_limit()
        time.sleep(60)
    return


# Returns data from a call to a url
def fetch(url):

    global api_call
    pause_if_limit_exceeded()

    try:
        # print url
        req = urllib2.Request(url)
        req.add_header("Accept","application/vnd.github.v3+json")
        resp = urllib2.urlopen(req)
        # data = json.loads(json_url.read())
        data = json.loads(resp.read())
        # api_call -= 1
        return data

    except Exception as er:
        print 'Error on Fetch Function: (' + str(er.message) + ')'
        return None

# req = urllib2.Request('http://www.example.com/')
# req.add_header('param1', '212212')
# req.add_header('param2', '12345678')
# req.add_header('other_param1', 'sample')
# req.add_header('other_param2', 'sample1111')
# req.add_header('and_any_other_parame', 'testttt')
# resp = urllib2.urlopen(req)
# content = resp.read()



def convert_data_to_list(itm):
    listt = ""
    for d in range(0, len(itm)):
        x = str(itm[d]['url'])
        print x
        listt += x+"\n"

    return listt


def fetch_topics(topic):
    global api_call
    api_call = git_api_rate_limit()
    url = 'https://api.github.com/search/repositories?q=topic:'+topic

    file = open("robotics-programming.txt","w")

    list_url = ""

    count = 0
    try:
        page = 1
        data = fetch(add_url_query(url, page, False))
        items = data['items']
        list_url += str(convert_data_to_list(items))+"\n"
        count += 1
        while len(items) == 100:
            page += 1
            data = fetch(add_url_query(url, page, False))
            items = data['items']
            list_url += str(convert_data_to_list(items))+"\n"
            count += 1
            if count == 10:
                break
        print 'done'

    except Exception as er:
        file.write(list_url)
        print er.message

    file.write(list_url)
    file.close()


def fetch_repo_topic_list(repo_url):
    try:
        data = fetch(add_url_query(repo_url+'/topics', 1, True))
        pprint.pprint(data)

    except Exception as er:
        print er.message


# The main function
if __name__ == "__main__":
    fetch_topics('computer-vision')
    # api_call = git_api_rate_limit()
    # print api_call
    # fetch_repo_topic_list('https://api.github.com/repos/akhilthomas17/reinforced_visual_slam')

# ros
# ros2
# robotics
# robotic
# robot
# deeplearning
# reinforcementlearning
# artificial
# machine-learning
# robotics-programming
# astar
# computer-vision
