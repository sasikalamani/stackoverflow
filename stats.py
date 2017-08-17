import rand
import csv
import random
import matplotlib.pyplot as plt

from collections import Counter

(quesAns, ansQues) = rand.qa()
#print(len(quesAns))  144306

#questions with more than 5 answers
count = 0
#answer = []
keys = []
for key in quesAns:
    if (len(quesAns[key]) >= 5):
        count += 1
        #answer = answer + quesAns[key]
        keys = keys + [key]


test = list()
train = list()
testDict = dict()
random.seed(2)
ranNum = random.sample(range(2126), 425)
for i in range(2126):
    if (i in ranNum): 
        test.append(keys[i])
    else:
        train.append(keys[i])



trainAns = []
for key in train:
    trainAns = trainAns + quesAns[key]


testAns = []
for key in test:
    testAns = testAns + quesAns[key]
    testDict[key] = quesAns[key]


#print(count)  #2126
#print(len(answer)) #12723

new = dict()
score = dict()
with open('Answers.csv', 'rb') as csvfile1:
    reader1 = csv.reader(csvfile1)
    for row in reader1:
        ansId = row[0]
        ansUser = row[1]
        ansScore = row[3]
        new[ansId] = ansUser
        score[ansId] = ansScore

#contains the list of answerers
answerers = []
scores = []
questions = []
trainScores = []
trainQuestions = []
trainAll = []
for ans in trainAns:
    trainQuestions.append(ansQues[ans])
    questions.append(ansQues[ans])
    au = new[ans]
    sc = int(score[ans])
    if(au not in answerers):
        answerers.append(au)
    trainAll.append(au)
    scores.append(sc)
    trainScores.append(sc)

testScores = []
testQuestions = []
testAll = []
for ans in testAns:
    testQuestions.append(ansQues[ans])
    questions.append(ansQues[ans])
    au = new[ans]
    sc = int(score[ans])
    if(au not in answerers):
        answerers.append(au)
    testAll.append(au)
    scores.append(sc)
    testScores.append(sc)

def ques():
    return testQuestions
def data():
    return (trainScores, trainQuestions, trainAll, 
            testScores, testQuestions, testAll, answerers, questions)

for key in testDict:
    for i in range(len(testDict[key])):
        testDict[key][i] = int(score[testDict[key][i]])

def dict():
    return testDict

# cnt = Counter()
# for i in range(len(scores)):
#    scr = scores[i]
#    cnt[scr] += 1

# #print(len(cnt))

# x = []
# y = []
# for key in cnt:
#     x.append(key)
#     y.append(cnt[key])

# print(x, y)

# plt.scatter(x, y)
# plt.ylabel('frequency')
# plt.xlabel('score')
# plt.show()

#print(len(questions))

#print(len(scores))

#print(len(answerers))  #4762


