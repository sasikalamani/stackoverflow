import MLP
import numpy


(ranks, output) = MLP.test_mlp()
ranks = ranks[0]
print(len(ranks))
print(len(ranks[0]))


accu = 0
for i in range(len(output)):
    num = output[i]
    count = 1
    for j in range(len(ranks[i])):
        if(ranks[i][j] == num):
            accu = accu + (1 / float(103-count))
            break
        count += 1
print(accu)



