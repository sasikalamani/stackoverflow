import csv
import stats
from collections import Counter
import nltk
#from keras.preprocessing.text import Tokenizer

(scores, questions, answerers, allAnswerers) = stats.data()

#print(len(scores))

for i in range (len(scores)):
    if(scores[i]<0):
        scores[i] = 0
    elif (scores[i]>500):
        scores[i] = 101
    else:
        while(scores[i] % 5 != 0):
            scores[i] += 1
        num = scores[i] // 5
        scores[i] = num


def mapUser(someList):
    userDict = Counter()
    usrs = 0
    for i in range(len(someList)):
       word = someList[i]
       if(word not in userDict):
        userDict[word] = usrs
        usrs += 1
    return userDict


userDict = mapUser(answerers)



titleDict = dict()
with open('Questions.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        titleDict[row[0]] = row[2]


for i in range(len(questions)):
    ques = questions[i]
    questions[i] = titleDict[ques]

cnt = Counter()
for title in questions:
    token = nltk.word_tokenize(title.decode("utf8", 'ignore'))
    for word in token:
        cnt[word.lower()]+= 1
#print(len(cnt)) 2765

index = dict()
i = 0
for k in cnt.keys():
    index[k] = i
    i+=1


inputs = [ ([0] * 7527) for row in range(len(questions)) ]

lineNum = 0
for sent in questions:
    lineNum +=1 
    token = nltk.word_tokenize(sent.decode("utf8", 'ignore'))
    for word in token:
            lookup = index[word.lower()]
            inputs[lineNum-1][lookup]= 1




for i in range(len(allAnswerers)):
    ID = userDict[allAnswerers[i]]
    newNum = ID+2765
    inputs[i][newNum] = 1

def inout():
    return(inputs, scores)



# tokenizer = Tokenizer(nb_words=MAX_NB_WORDS)
# tokenizer.fit_on_texts(questions)
# inputs = tokenizer.texts_to_matrix(questions)
