Codes are for knn,kmeans,hac are in hw2_data folder ,named knn.py,kmeans.py and hac.py respectively.

For knn after running the script it will calculate accuracy for k=1,..,199 by using k-fold
cross validation=10.After these calculations script gonna plot these values and when you exit
plotted figure window its gonna print best k value and gonna test this k value with given test 
data and print its accuracy for that given k.

For kmeans I have wrote function kmeans that takes k and data as input and returns centroids,
data and objective func value as a list.To plot obj function value for k I have wrote plotobjfunction
which takes input(numpy data) and by restarting 10 times for same k I take avg of those obj. function
values that I return from kmeans function. After deciding k, I have wrote function plotclusters which
take k and data as input and plots clusters with different clusters and shows clusters centroids by
red stars.For ex, at the end of code you can call plotobjfunction(clustering1) and plot the avg valued
obj functions for k=1,..,10. And after deciding k you can call plotclusters(2,clustering1) you can plot
clusters and centroids.

For hac I have wrote function hac that takes three input ,criterion which i used as string(for single
linkage "single",complete linkage "complete" and so on), k which is integer that determines number 
of clusters that my hac has to stop at, and data which is our numpy datas namely data1,..,data4.
As output hac will return set of clusters and you can feed these clusters into plotclusters function
which will take clusters as input and plots them. 
