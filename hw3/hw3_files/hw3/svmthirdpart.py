from sklearn.svm import SVC
import numpy as np
from sklearn.model_selection import GridSearchCV

train_data=np.load('hw3_data/catdog/train_data.npy')
train_labels=np.load('hw3_data/catdog/train_labels.npy')
test_data=np.load('hw3_data/catdog/test_data.npy')
test_labels=np.load('hw3_data/catdog/test_labels.npy')




def gridsearch(train_data):
    train_data=train_data/255
    parameters={'C':[0.01,0.1  ,1  ,10 , 100],
            #'gamma':[ 0.00001,0.0001,0.001,0.01,0.1,1],
            'kernel':['linear']
                }
    clf=GridSearchCV(SVC(),parameters,verbose=2,cv=5)
    clf.fit(train_data,train_labels)
    means = clf.cv_results_['mean_test_score']
    for mean, params in zip(means,clf.cv_results_['params']):
        print("%0.3f  for %r "% (mean, params))



def test(kernel_p,gamma_p,C_p,train_data,train_labels,test_data,test_labels):
    train_data=train_data/255
    classifier=SVC(kernel=kernel_p,gamma=gamma_p,C=C_p)
    classifier.fit(train_data,train_labels)
    test_data=test_data/255
    #print(classifier.get_params())
    print(classifier.score(test_data,test_labels))

#gridsearch(train_data)
test('rbf',0.01,10,train_data,train_labels,test_data,test_labels)
#test('rbf',0.01,100,train_data,train_labels,test_data,test_labels)
