# Automated-Content-Grading-Using-Machine-Learning
Grading of examination papers is a hectic, time-labor intensive task and is often subjected to inefficiency and bias in checking. This research project is a primitive experiment in automation of grading of theoretical answers written in exams by students in technical courses which yet had continued to be human graded. In this project, we show how algorithmic approach in machine learning can be used to automatically examine and grade theoretical content in exam answer papers. Bag of words, their vectors & centroids and a few semantic and lexical text features have been used overall. Machine learning models have been implemented on datasets manually built from exams given by graduating students enrolled in technical courses. These models have been compared to show the effectiveness of each model.


# Motivation
Many organizations and educational institutions have already introduced computer based tests, even for text based exams. Our project aims at solving the problem of automated grading of these tests. Also, text based content from hand written papers (after OCR to text processing), can similarly be checked and graded as well, although research on this is in progress.
# Hypothesis & Challenges
* Technical domain
As many systems are developed already to solve general content, e.g. Grading of English essays, etc; our approach is to solve the content in technical domain, which had not yet been successfully attempted to be solved. Technical domain would include courses like Bachelor of Science, Master of Science, Bach. Of Technology & Engineering, Arts, etc. and not General English based, e.g. Psychology, Law etc.
* Computer Based Tests
The exams of whom the content is to be graded by this approach will give us text input through the computer based examination. Many organizations today are adopting computer based exams.
* Data collected
Only the “theoretical content” can be graded using this approach is to be graded, as it takes about 75-85% of total time for a human grader to check and grade a paper for only the theoretical content. Checking of other types of content, e.g. Illustrative, diagrammatic, numeric etc. takes a very jiffy amount of time as compared to theoretical content. As a result, we can achieve significant amount of time being reduced while checking the theoretical content i.e. an expected 60-80% reduction in time spent by a human grader as compared to a computer grading system.
* Large collection of data:
As the content to be checked for human graders is generally large, it is expected that this system be implemented on domains with huge data content to be processed

# Software tools used
We chose to implement our model in Python 2.7.x, as there is a vast set of libraries for working with natural language processing. We have used the Natural Language Toolkit (NLTK) and textmining for most NLP tasks. Other libraries: numpy, scipy, xlrd, xlwt, word2vec etc. have been used for various tasks.


## Authors
* **Rahul Chauhan**
* **Ravinder Saharan**
* **Siddhartha Singh**
