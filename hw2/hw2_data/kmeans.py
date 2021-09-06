import numpy as np

import matplotlib.pyplot as plt

clustering1=np.load("hw2_data/kmeans/clustering1.npy")
clustering2=np.load("hw2_data/kmeans/clustering2.npy")
clustering3=np.load("hw2_data/kmeans/clustering3.npy")
clustering4=np.load("hw2_data/kmeans/clustering4.npy")
#print(clustering1)


arr=np.array([[1,2],
                [2,5],
                [3,9],
                [15,26],
                [-1,6],
                [8,3],
                [4,-9],
                [1,1],
                [-3,3]])
#print(arr)
"""
minxy=np.amin(arr,axis=0)
maxxy=np.amax(arr,axis=0)

x=np.array([1,2,3,4])
y=np.array([5,6,7,8])
x.resize(len(x),1)
x.resize(len(y),1)
cents=np.column_stack((x,y))"""
def euclid_distance(vector1,vector2):
    distance=0.0
    length=len(vector1)
    for i in range(length):
        distance+= (vector1[i]-vector2[i])**2
    return distance**0.5    

def initcenters(k,data):
    minxy=np.amin(data,axis=0)
    maxxy=np.amax(data,axis=0)
    #print(minxy)
    #print(maxxy)
    x_coordinates=np.random.uniform(minxy[0],maxxy[0],k)
    y_coordinates=np.random.uniform(minxy[1],maxxy[1],k)
    x_coordinates.resize(len(x_coordinates),1)
    y_coordinates.resize(len(y_coordinates),1)
    centroids=np.column_stack((x_coordinates,y_coordinates))
    return centroids

def closest_centroid(points,centroids):
    distances=np.sqrt(((points - centroids[:, np.newaxis])**2).sum(axis=2)) 
    return np.argmin(distances,axis=0)                    #this will return list of centroids which
                                                          #has smallest distance to our points


def kmeans(k,data):                                       #returns data,labels and obj func value
    cents=initcenters(k,data)
    #print(cents)
    #print(closest_centroid(clustering1,cents))
    close_cents=closest_centroid(data,cents)
    #print(close_cents)
    new=np.column_stack((data,close_cents))
    #print(new)
    #print(len(close_cents))
    #print(close_cents)
    ln=len(close_cents)
    while 1:
        newx=[]
        newy=[]
        for i in range(k):
            newx.append([])
            newy.append([])
            for j in range(ln):
                if int(new[j][-1])==i:
                    newx[i].append(new[j][0])
                    newy[i].append(new[j][1])
        xs=[]
        ys=[]
        
        for i in range(k):
            tmp1=np.mean(newx[i],axis=0)
            tmp2=np.mean(newy[i],axis=0)
            if(np.isnan(tmp1)):                        #nan check
                xs.append(0)
            else:
                xs.append(tmp1)
            if(np.isnan(tmp2)):
                ys.append(0)
            else:
                ys.append(tmp2)
            #    print("i and newx[i]:",i,newx[i])
            #print("here")
            #xs.append(tmp1)
            #print("here1")
            #ys.append(tmp2)
        newcents=np.column_stack((xs,ys))
        #print("here")
        #print(newcents)
        listofcentsforeachdata=closest_centroid(data,newcents)#todo
        #print(listofcentsforeachdata)
        if np.array_equal(listofcentsforeachdata, close_cents):         #if centroid assigments didnt change stop
            new[:,2]=listofcentsforeachdata
            break
        else:
            new[:,2]=listofcentsforeachdata                         
            close_cents=listofcentsforeachdata
            continue
    #print("hi")
    dataandclusterslen=len(new)
    s=0
    #print(new[0][0:3])
    for i in range(dataandclusterslen):
        s+=(euclid_distance(new[i][0:2],newcents[int(new[i][2])]))**2
    return [newcents,new,s/2.0]
    """plt.figure(figsize=(11,5))
    for i in range(dataandclusterslen):
        if int(new[i][2])==0:
            plt.scatter(new[i][0],new[i][1],c='g',s=3)
        if int(new[i][2])==1:
            plt.scatter(new[i][0],new[i][1],c='b',s=3)
        if int(new[i][2])==2:
            plt.scatter(new[i][0],new[i][1],c='y',s=3)
    for i in range(k):
        plt.scatter(newcents[i][0],newcents[i][1],marker='*',c='r',s=300)
    plt.show()"""
#initcenters(10,arr)
#res=kmeans(2,clustering1)
def plotobjfunction(data):
    restarthowmany=10
    kobjlist=[]
    for k in range(1,11):           #this one for k=1,..,10
        tot=0
        for i in range(restarthowmany):         #for restarting kmeans to avg obj function
            #print("k i:",k," ",i)
            obj=kmeans(k,data)
            tot+=obj[2]
        kobjlist.append(tot/restarthowmany)
    #print(kobjlist)
    plt.xlabel('k')
    plt.ylabel('obj')
    plt.plot(list(range(1,11)),kobjlist,'b',marker='o',markersize=6)
    plt.show()

def plotclusters(k,data):
    res=kmeans(k,data)
    newcents=res[0]
    new=res[1]
    dataandclusterslen=len(new)
    plt.figure(figsize=(8.25,6))
    for i in range(dataandclusterslen):
        if int(new[i][2])==0:
            plt.scatter(new[i][0],new[i][1],c='g',s=3)
        if int(new[i][2])==1:
            plt.scatter(new[i][0],new[i][1],c='b',s=3)
        if int(new[i][2])==2:
            plt.scatter(new[i][0],new[i][1],c='orange',s=3)
        if int(new[i][2])==3:
            plt.scatter(new[i][0],new[i][1],c='y',s=3)
        if int(new[i][2])==4:
            plt.scatter(new[i][0],new[i][1],c='purple',s=3)
    for i in range(k):
        plt.scatter(newcents[i][0],newcents[i][1],marker='*',c='r',s=300)
    plt.show()


#plotobjfunction(clustering4)
plotclusters(5,clustering4)


