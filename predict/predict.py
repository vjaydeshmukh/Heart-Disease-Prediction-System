import numpy as np
from sklearn import tree

input_data = open("D:\\NOTES\\PROJECT\\heart\\predict\\heart.csv", "r").read().split("\n")
features = input_data[0].split(",")

del features[-1] # delete target attribute from feature list
del input_data[0] # delete feature list to get raw data
del input_data[-1] # remove extra line that is present in the raw data

samples = [] # to store all raw data of features only
sample_classes = [] # to store raw data of target attribute only


def cancer_enum(target):
	if target == 1:
		return 1
	else:
		return 0

for i, line in enumerate(input_data):
	data = line.split(",") # separating every row of raw data
	target = int(data[-1]) # get target value from data
	del data[-1]  # remove target value from data
	samples.append(data)
	sample_classes.append(cancer_enum(target))

clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(samples, sample_classes)

def predict(user_input):
	input_data = np.array(user_input).reshape(1, -1)
	result = clf.predict(input_data)
	if result == 0:
		return "false"
	else:
		return "true"
