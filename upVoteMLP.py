import csv
import stats
from collections import Counter
import nltk
#from keras.preprocessing.text import Tokenizer

(trainScores, trainQuestions, trainAll, 
        testScores, testQuestions, testAll, answerers, questions) = stats.data()

#print(len(scores))
#makes the output scores into a classfication problem. Negatives scores 
#are made 0, and above 500 is made 101. All others are split in 5
#range sections.
def scorize(scores):
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
    return scores

trainScores = scorize(trainScores)
testScores = scorize(testScores)

#maps an index for each user in the list
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
for i in range(len(trainQuestions)):
    ques = trainQuestions[i]
    trainQuestions[i] = titleDict[ques]
newTQ  = [0] * len(testQuestions)
for i in range(len(testQuestions)):
    ques = testQuestions[i]
    newTQ[i] = titleDict[ques]


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


train = [ ([0] * 7527) for row in range(len(trainQuestions)) ]
test = [ ([0] * 7527) for row in range(len(newTQ)) ]


#creates the one hot encoding of the title as well as the answerer
def inputize(questions, allAnswerers, inputs):
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
    return inputs

train = inputize(trainQuestions, trainAll, train)
test = inputize(newTQ, testAll, test)

def inout():
    return(train, test, trainScores, testScores)



# tokenizer = Tokenizer(nb_words=MAX_NB_WORDS)
# tokenizer.fit_on_texts(questions)
# inputs = tokenizer.texts_to_matrix(questions)
