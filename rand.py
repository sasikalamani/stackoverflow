import random
import csv
from collections import Counter
import nltk

x = 1000 * [0]
ques = 1000 * [0]
user = 1000 * [0]
body = 1000 * [0]
score = 1000 * [0]


#selects a random 1000 questions
random.seed(10)
ranNum = random.sample(range(172782), 1000)


#the array x contains the selected 1000 questions
cnt = 0
num = 0 
quesUser = dict()
quesBody = dict()
quesScore = dict()
with open('Questions.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if(num in ranNum):
            x[cnt] = row
            cnt += 1
            quesUser[row[0]] = row[1]
            quesBody[row[0]] = row[3]
            quesScore[row[0]] = row[4]
        num += 1

#separates the ques, user, body, and score of the 1000 sample
for i in range(len(x)):
    ques[i] = x[i][0]
    user[i] = x[i][1]
    body[i] = x[i][3]
    score[i] = x[i][4]


#puts the users in a dictionary and maps it to a index number
userDict = Counter()
usrs = 0
for i in range(len(user)):
   word = user[i]
   if(word not in userDict):
    userDict[word] = usrs
    usrs += 1
#print(len(userDict))  960 users




#tokenizing the bodies
string = ""
for i in range(len(body)):
    string = string + body[i]

tokens = nltk.word_tokenize(string.decode('utf-8', 'ignore'))

#makes them all lowercase
for i in range(len(tokens)):
    tokens[i] = tokens[i].lower()

#puts the words in a counter
cnt = Counter()
for i in range(len(tokens)):
   word = tokens[i]
   cnt[word]+= 1
#print(len(cnt))


#maps each word to an index number
index = dict()
i = 0
for k in cnt.keys():
    index[k] = i
    i+=1



#returns a dictionary that given a question returns
#all the answers to that questions
def qa():
    quesAns = dict()
    ansQues = dict()
    with open('Question-Answer.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            question = row[1]
            if(question not in quesAns):
                quesAns[question] = [row[0]]
            else:
                cur = quesAns.get(question)
                new = cur + [row[0]]
                quesAns[question] = new

            answer = row[0]
            ansQues[answer] = question
    return(quesAns, ansQues)


#answers contains all the answerIDs for the sample
quesAns, ansQues = qa()
answers = []
for question in ques:
    if(question not in quesAns):
        ques.remove(question)
        continue
    answers = answers + quesAns[question]



#new maps the answer to the user
new = dict()
with open('Answers.csv', 'rb') as csvfile1:
    reader1 = csv.reader(csvfile1)
    for row in reader1:
        ansId = row[0]
        ansUser = row[1]
        new[ansId] = ansUser

#contains the list of answerers
answerers = []
for answer in answers:
    au = new[answer]
    if(au not in answerers):
        answerers.append(au)


#maps the answerers to an index
ansIndex = dict()
i1 = 0
for k in answerers:
    ansIndex[k] = i1
    i1+=1

output = [0] * len(answers)
for i in range(len(answers)):
    answerer = new[answers[i]]
    output[i] = ansIndex[answerer]



questions = len(answers) * [0]
for i in range(len(answers)):
    answer = answers[i]
    questions[i] = ansQues[answer]

usrIn = len(questions) * [0]
bodyIn = len(questions) * [0]
for i in range(len(questions)):
    userInput = quesUser[questions[i]]
    bdIn = quesBody[questions[i]]
    usrIn[i] = userInput
    bodyIn[i] = bdIn


#makes one of the input arrays
rows = len(questions)
cols = len(userDict.keys())  
userIn = [ ([0] * cols) for row in range(rows) ]

for i in range(len(usrIn)):
    ID = userDict[usrIn[i]]
    userIn[i][ID] = 1


quesIn = [ ([0] * 8064) for row in range(rows) ]

lineNum = 0
for sent in bodyIn:
    lineNum +=1 
    token = nltk.word_tokenize(sent.decode("utf8", 'ignore'))
    for word in token:
            lookup = index[word.lower()]
            quesIn[lineNum-1][lookup]= 1





def allInputs():
    test1 = list()
    test2 = list()
    testO = list()
    train1 = list()
    train2 = list()
    trainO = list()
    valid1 = list()
    valid2 = list()
    validO = list()

    count = 0
    random.seed(2)
    ranNum = random.sample(range(1094), 200)
    for i in range(1094):
        if (i in ranNum and count<100): 
            test1.append(quesIn[i])
            test2.append(userIn[i])
            testO.append(output[i])
            count = count+1
        elif (i in ranNum):
            valid1.append(quesIn[i])
            valid2.append(userIn[i])
            validO.append(output[i])
        else:
            train1.append(quesIn[i])
            train2.append(userIn[i])
            trainO.append(output[i])
    return(test1, test2, testO, train1, train2, trainO, valid1, valid2, validO)




