import numpy as np
from sklearn.svm import SVC
from draw import draw_svm

train_data=np.load('hw3_data/nonlinsep/train_data.npy')
train_labels=np.load('hw3_data/nonlinsep/train_labels.npy')

x1_min=np.min(train_data,axis=0)[0]
x1_max=np.max(train_data,axis=0)[0]
x2_min=np.min(train_data,axis=0)[1]
x2_max=np.max(train_data,axis=0)[1]
classifier=SVC(kernel='sigmoid')     #change kernel
classifier.fit(train_data,train_labels)

draw_svm(classifier,train_data,train_labels,x1_min,x1_max,x2_min,x2_max)
