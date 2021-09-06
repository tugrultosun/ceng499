from sklearn.svm import SVC
import numpy as np
train_data=np.load('hw3_data/catdogimba/train_data.npy')
train_labels=np.load('hw3_data/catdogimba/train_labels.npy')
test_data=np.load('hw3_data/catdogimba/test_data.npy')
test_labels=np.load('hw3_data/catdogimba/test_labels.npy')


classifier=SVC(kernel='rbf',C=1)
train_data=train_data/255
#classifier.fit(train_data,train_labels)
#print(classifier.score(test_data/255,test_labels))

print(train_labels)

