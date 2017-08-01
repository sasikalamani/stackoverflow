import rand
import csv
import matplotlib.pyplot as plt

from collections import Counter

(quesAns, ansQues) = rand.qa()
#print(len(quesAns))  144306
count = 0
answer = []
for key in quesAns:
    if (len(quesAns[key]) >= 5):
        count += 1
        answer = answer + quesAns[key]

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
al = []
for ans in answer:
    questions.append(ansQues[ans])
    au = new[ans]
    sc = int(score[ans])
    if(au not in answerers):
        answerers.append(au)
    al.append(au)
    scores.append(sc)


def data():
    return (scores, questions, answerers, al)

cnt = Counter()
for i in range(len(scores)):
   scr = scores[i]
   cnt[scr] += 1

#print(len(cnt))

x = []
y = []
for key in cnt:
    x.append(key)
    y.append(cnt[key])

#print(x, y)

#plt.scatter(x, y)
#plt.ylabel('frequency')
#plt.show()

#print(len(questions))

#print(len(scores))

#print(len(answerers))  #4762


