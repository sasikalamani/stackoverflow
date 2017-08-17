# stackoverflow

Preprocessing the data:
rand.py    -   selects a random sample of 1000 questions from the R dataset

Removes all the questions without answers. The input to the neural net is the body of the question in one hot encoding as well as the user who asked the question. The input size is 8064 features.

The output of the MLP was a 611 classification problem that predicted which user would answer the question.

To run the preprocessing file, files needed:
Questions.csv
Question-Answer.csv
Answers.csv

run using the command : python rand.py

stats.py  -  calculates statistics on the R dataset like how many questions have 5 or more answers.

Creates a train and test dataset from this subset.

Also, graphs certain statistics such as the distribution of scores.

To run the preprocessing file, files needed:
Answers.csv

run using the command : python stats.py

upVoteMLP.py  - preprocesses the data for the R dataset.

The input features are the tags in one hot encoding as well the answerer in one hot encoding. The input size is 7527.

The output is the score made into a classification problem. There are 102 classes therefore the output size is 102.

To run the preprocessing file, files needed:
Questions.csv
stats.py

run using the command : python upVoteMLP.py




Neural Nets:
MLP.py     -  a simple multi-layered perceptron
add or remove hidden layers with the hidden layer class
tune the hyper parameters with number of hidden units, learning rate, number of epochs, etc.

Validation set is currently set to be the same as the train set.

Will print the test error for epochs that see a significant change.
In the end, will print the best validation error and test error.

To run the neural net file, files needed:
upVoteMLP.py
logistic_sgd.py (for the logistic regression layer)

run using the command : python MLP.py


sparseMLP.py - a mulit-layered perceptron modeled after the Hinton distributed learning paper. The MLP has two separate inputs. The second layer is separate distributed encoding of the two inputs. There are multiple combined hidden layers with a final output.

Validation set is currently set to be the same as the train set.

Will print the test error for epochs that see a significant change. In the end, will print the best validation error and test error.

To run the neural net file, files needed: 
rand.py 
logistic_sgd.py (for the logistic regression layer)

run using the command : python sparseMLP.py




Post Processing the data:
accu.py    - calculates the MRR accuracy of the prediction of the MLP vs the ground truth

To run the post processing file, files needed:
MLP.py

run using the command : python accu.py

post.py   - calculates and prints the MRR accuracy for the MLP for the test set

To run the post processing file, files needed:
stats.py
MLP.py

run using the command : python post.py