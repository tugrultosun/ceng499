import numpy as np
from statistics import mode
import matplotlib.pyplot as plt

train_data=np.load("hw2_data/knn/train_data.npy")
train_labels=np.load("hw2_data/knn/train_labels.npy")
test_data=np.load("hw2_data/knn/test_data.npy")
test_labels=np.load("hw2_data/knn/test_labels.npy")


train_data_with_labels=np.column_stack((train_data,train_labels))           #concatenating datas and labels
test_data_with_labels=np.column_stack((test_data,test_labels))
#print(train_data_with_labels)

#print(train_data[0:5])
#print(train_labels[0:5])
#print(train_data_with_labels[0:5])
#for i in range(len(train_data_with_labels)-1):
 #   print(train_data_with_labels[i])




def keyDistanceforNeighborList(data):               #key for sort function
    return data[1]

def keyKandAccuracyList(data):
    return data[1]

def KNN(k,train_set,valid_set):
    correct_prediction=0
    total_prediction=0
    for row_vi,row_valid in enumerate(valid_set):
        total_prediction+=1
        neighbor_list=[]
        correct_label=row_valid[-1]
        for row_ti,row_test in enumerate(train_set):
            total_distance=0.0
            label=row_test[len(row_test)-1]
            total_distance=euclid_distance(row_valid,row_test)
            info_list=[]
            info_list.append(row_ti)
            info_list.append(total_distance)
            info_list.append(label)
            neighbor_list.append(info_list)
        neighbor_list.sort(key=keyDistanceforNeighborList)    #sort neighbors based on distance(which is second column)
        labels_of_neighbors=[]
        for i in range(k):
            labels_of_neighbors.append(neighbor_list[i][2])   #adding neighbor labels into a list
        predicted_label=mode(labels_of_neighbors)             #mode returns most occurence element in a list
        if correct_label==predicted_label:
            correct_prediction+=1
    accuracy=correct_prediction/total_prediction
    return accuracy                             #return accuracy for given train and valid set and k
    
def find_k(data):
    number_of_folds=10
    fold_size=round(len(data)/number_of_folds)
    #print(fold_size)
    train_data=[]
    val_data=[]
    for i in range(number_of_folds):
        train_list=[]
        val_list=[]
        for j,row in enumerate(data):
            if(i*fold_size)<=j < (i+1)*fold_size:
                val_list.append(row)
            else:
                train_list.append(row)
        train_data.append(train_list)
        val_data.append(val_list)

    k_and_accuracy_list=[]
    for k in range(1,200,2):
        total_accuracy=0.0
        for f in range(number_of_folds):
            accuracyforcurrentfold=KNN(k,train_data[f],val_data[f])
            total_accuracy+=accuracyforcurrentfold
        currenttest=[]
        currenttest.append(k)
        currenttest.append(total_accuracy/number_of_folds)
        k_and_accuracy_list.append(currenttest)
    klist=[]
    acclist=[]
    for i in range(len(k_and_accuracy_list)):
        klist.append(k_and_accuracy_list[i][0])
        acclist.append(k_and_accuracy_list[i][1])
    plt.figure(figsize=(11,5))
    plt.plot(klist,acclist,'b',markersize=3)
    plt.xlabel("k")
    plt.ylabel("accuracy")
    plt.show()
    k_and_accuracy_list.sort(key=keyKandAccuracyList, reverse=True)
    return k_and_accuracy_list[0][0]
            



#print(train_data[0])
#print(train_data)
#print(train_data.shape)
#print(train_labels.shape)

#print(mode([1,2,3,3,5,8,9,11,11,2,3]))
#batch=round(len(train_data)/number_of_folds)
#print(batch)       

def euclid_distance(vector1,vector2):
    distance=0.0
    length=len(vector1)
    for i in range(length):
        distance+= (vector1[i]-vector2[i])**2
    return distance**0.5


"""vector=[0,0]
vectorr=[6,8]
print(euclid_distance(vector,vectorr))"""

#print(euclid_distance(train_data[0],train_data[1]))
best_k=find_k(train_data_with_labels)               #this will find best k from train data
#print(type(best_k))
print("best k is ",best_k)
accuracy_for_best_k=KNN(best_k,train_data_with_labels,test_data_with_labels) #gonna calc acc for best k we found
print("accuracy for test data is: ",accuracy_for_best_k)
