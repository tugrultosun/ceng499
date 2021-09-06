import numpy as np
import matplotlib.pyplot as plt

data1 = np.load("hw2_data/hac/data1.npy")
data2 = np.load("hw2_data/hac/data2.npy")
data3 = np.load("hw2_data/hac/data3.npy")
data4 = np.load("hw2_data/hac/data4.npy")

#print(data1)

def euclid_distance(vector1,vector2):
    distance=0.0
    length=len(vector1)
    for i in range(length):
        distance+= (vector1[i]-vector2[i])**2
    return distance**0.5

def initclusters(data):
    initialized_clusters=[]
    ln=len(data)
    for i in range(ln):
        #print(data[i])
        tmp=[]
        tmp.append(data[i].tolist())
        initialized_clusters.append(tmp)
    return initialized_clusters


def merge(active_cluster,index1,index2):
    merged_cluster=[]
    for point1 in active_cluster[index1]:
        merged_cluster.append(point1)
    for point2 in active_cluster[index2]:
        merged_cluster.append(point2)
    return merged_cluster




#single linkage criterion, returns index of clusters to be merged
def single(active_clusters):
    index1=0
    index2=0
    min_distance=np.inf
    for ix,data1 in enumerate(active_clusters):
        for iy,data2 in enumerate(active_clusters):
            if ix==iy:                      #same clusters so continue
                continue
            else:
                for point1 in data1:
                    for point2 in data2:
                        if euclid_distance(point1,point2)<min_distance:
                            min_distance=euclid_distance(point1,point2)
                            index1=ix
                            index2=iy
    return [index1,index2]

#complete linkage criterion, returns index of clusters to be merged
def complete(active_clusters):
    index1=0
    index2=0
    min_distance=np.inf
    for ix,data1 in enumerate(active_clusters):
        for iy,data2 in enumerate(active_clusters):
            if ix==iy:                      #same clusters so continue
                continue
            else:
                local_max=-1
                for point1 in data1:
                    for point2 in data2:
                        if euclid_distance(point1,point2)>local_max:
                            local_max=euclid_distance(point1,point2)
                if local_max<min_distance:
                    min_distance=local_max
                    index1=ix
                    index2=iy
    return [index1,index2]

#average linkage criterion, returns index of clusters to be merged
def average(active_clusters): 
    index1=0
    index2=0
    min_avg=np.inf
    for ix,data1 in enumerate(active_clusters):
        for iy,data2 in enumerate(active_clusters):
            if ix==iy:                      #same clusters so continue
                continue
            else:
                total=0.0
                for point1 in data1:
                    for point2 in data2:
                        total+=euclid_distance(point1,point2)
                avg=total/(len(data1)*len(data2))
                if avg<min_avg:
                    min_avg=avg
                    index1=ix
                    index2=iy
    return [index1,index2]

def centroid(active_clusters):
    index1=0
    index2=0
    min_distance=np.inf
    #N=[0,0]
    #M=[0,0]
    for ix,data1 in enumerate(active_clusters):
        for iy,data2 in enumerate(active_clusters):
            if ix==iy:                      #same clusters so continue
                continue
            else:
                N=[0,0]
                M=[0,0]
                for point1 in data1:
                    N[0]+=point1[0]
                    N[1]+=point1[1]
                N[0]=N[0]/len(data1)
                N[1]=N[1]/len(data1)
                for point2 in data2:
                    M[0]+=point2[0]
                    M[1]+=point2[1]
                M[0]=M[0]/len(data2)
                M[1]=M[1]/len(data2)
                curr_distance=euclid_distance(N,M)
                if curr_distance<min_distance:
                    min_distance=curr_distance
                    index1=ix
                    index2=iy
    return [index1,index2]

#k is number of clusters here
def hac(criterion,k,data):                  
    active_set=initclusters(data)
    active_number_of_clusters=len(active_set)
    if criterion=="single":
        while active_number_of_clusters>k:
            indexes=single(active_set)
            merged_cluster=merge(active_set,indexes[0],indexes[1])
            indexes.sort(reverse=True)
            active_set.remove(active_set[indexes[0]])
            active_set.remove(active_set[indexes[1]])
            active_set.append(merged_cluster)
            active_number_of_clusters-=1
        return active_set
    elif criterion=="complete":
        while active_number_of_clusters>k:
            indexes=complete(active_set)
            merged_cluster=merge(active_set,indexes[0],indexes[1])
            indexes.sort(reverse=True)
            active_set.remove(active_set[indexes[0]])
            active_set.remove(active_set[indexes[1]])
            active_set.append(merged_cluster)
            active_number_of_clusters-=1
        return active_set
    elif criterion=="average":
        while active_number_of_clusters>k:
            indexes=average(active_set)
            merged_cluster=merge(active_set,indexes[0],indexes[1])
            indexes.sort(reverse=True)
            active_set.remove(active_set[indexes[0]])
            active_set.remove(active_set[indexes[1]])
            active_set.append(merged_cluster)
            active_number_of_clusters-=1
        return active_set
    elif criterion=="centroid":
        while active_number_of_clusters>k:
            indexes=centroid(active_set)
            merged_cluster=merge(active_set,indexes[0],indexes[1])
            indexes.sort(reverse=True)
            active_set.remove(active_set[indexes[0]])
            active_set.remove(active_set[indexes[1]])
            active_set.append(merged_cluster)
            active_number_of_clusters-=1
        return active_set
    
def plotclusters(clusters):
    if len(clusters)==2:
        cluster1=clusters[0]
        cluster2=clusters[1]
        for point1 in cluster1:
            plt.scatter(point1[0],point1[1],c='g')
        for point2 in cluster2:
            plt.scatter(point2[0],point2[1],c='b')
    if len(clusters)==4:
        cluster1=clusters[0]
        cluster2=clusters[1]
        cluster3=clusters[2]
        cluster4=clusters[3]
        for point1 in cluster1:
            plt.scatter(point1[0],point1[1],c='g')
        for point2 in cluster2:
            plt.scatter(point2[0],point2[1],c='b')
        for point3 in cluster3:
            plt.scatter(point3[0],point3[1],c='orange')
        for point4 in cluster4:
            plt.scatter(point4[0],point4[1],c='y')
    plt.show()



#########---TEST---############    
clusterdata=hac("centroid",4,data4)
plotclusters(clusterdata)
#print(initclusters(data1))
