from textblob import TextBlob
import urllib

positive_message = "In line 784 the condition makes not sense:\r\n`&& ~ei.pi->passed_pawns(strongSide)`\r\nThe **~** operator is a **bitwise not** not a **logical not**. So above condition can only be false if each square contains a passed pawn, which is impossible.\r\nI think you intend following condition:\r\n`&& !ei.pi->passed_pawns(strongSide)"
negative_message = "Very Bad!"


#TextBlob
#Polarity = [-1 , +1] +1 positive and -1 is negative
#Subjectivity = [0, 1] 0 is very objective, and 1 is very subjective
text = TextBlob(positive_message)
text2 = TextBlob(negative_message)
print text.sentiment
print text2.sentiment
# print text.sentiment.polarity



#URLLIB
data = urllib.urlencode({"text": positive_message})
u = urllib.urlopen("http://text-processing.com/api/sentiment/", data)
the_page = u.read()
print the_page
