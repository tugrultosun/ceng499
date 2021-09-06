My decision tree diagrams in pdf files is new version of algorithm which is for empty data I was returning
label of entire dataset instead of parent.I corrected the algorithm and made it to return label of parent dataset.

My decision tree code is in decisiontree.py file.

I have wrote functions to create trees named as id3withgainratio,id3withinfogain,id3withavgginindex,etc.
I have wrote function tester to print out accuracy of my tree model.
In last lines I call tree creation algorithm with those tree creation algorithms I named(I used same algorithm id3
but I didnt want to give another parameter to select attribute selection algorithm).
Algorithm will return a tree as dictionary type in python.Then with returned tree,
I created pdf file with graphviz using print_tree function.Lastly, I test accuracy of my tree on test dataset
by calling tester function.

For preprun part I compare chi square value of attribute with table and if it is 
smaller or equal then I return label of dataset and make tree stop growing.

For svm part written codes are in svmfirstpart,svmsecondpart and goes on like that..
For third part I have used gridsearchcv from sklearn.model_selection.I give parameters
with different kernels at each run instead of making them all run at one time as it
takes much time to train.