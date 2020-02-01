import json

from textblob import TextBlob
import urllib

t1 = "Very good!"
t2 = "the code looks just fine!"
t3 = "fine"


#TextBlob
#Polarity = [-1 , +1] +1 positive and -1 is negative
#Subjectivity = [0, 1] 0 is very objective, and 1 is very subjective
text = TextBlob(t1)
text2 = TextBlob(t2)
text3 = TextBlob(t3)
print text.sentiment
print text2.sentiment
print text3.sentiment
# print text.sentiment.polarity

print '*' * 100

#URLLIB
data = urllib.urlencode({"text": t1})
data2 = urllib.urlencode({"text": t2})
data3 = urllib.urlencode({"text": t3})
u = urllib.urlopen("http://text-processing.com/api/sentiment/", data)
u2 = urllib.urlopen("http://text-processing.com/api/sentiment/", data2)
u3 = urllib.urlopen("http://text-processing.com/api/sentiment/", data3)
# print u.read()
# print u2.read()
# print u3.read()

t = json.loads(u.read())
print t
