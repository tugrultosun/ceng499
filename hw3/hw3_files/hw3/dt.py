from math import log




def divide(data, attr_index, attr_vals_list):
    """Divides the data into buckets according to the selected attr_index.
    :param data: Current data in the node
    :param attr_index: Selected attribute index to partition the data
    :param attr_vals_list: List of values that attributes may take
    :return: A list that includes K data lists in it where K is the number
     of values that the attribute with attr_index can take
    """
    dividedlist=[]
    attributelist=attr_vals_list[attr_index]
    attributelistlen=len(attributelist)
    for i in range(attributelistlen):
        dividedlist.append([])
        for datum in data:
            if datum[attr_index]==attributelist[i]:
                dividedlist[i].append(datum)
    return dividedlist
    pass


def entropy(data, attr_vals_list):
    """
    Calculates the entropy in the current data.
    :param data: Current data in the node
    :param attr_vals_list: List of values that attributes may take
    (Last attribute is for the labels)
    :return: Calculated entropy (float)
    """
    s=0
    howmanyatt=len(attr_vals_list)-1
    totaldatalen=len(data)
    """for i in range(howmanyatt):
        setofvaluesthisattributecantake=attr_vals_list[i]
        #print(attr_vals_list[i])
        x=entropyhelperforithattribute(data,setofvaluesthisattributecantake,attr_vals_list[-1],i)
        print(x)"""
    subs=0
    howmuchdata=len(data)
    for label in attr_vals_list[-1]:
        c=0
        for datum in data:
            if datum[-1]==label:
                c+=1
        if c==0:
            continue
        else:
            subs+=(c/howmuchdata)*log(c/howmuchdata,2)
    subs*=-1
    #print(subs)
    return subs
    


def gainratiohelperforithattribute(data,attr_vals_list,index,value):
    s=0
    #howmanyclass=len(classlist)
    subs=0
    attributevalues=attr_vals_list[index]
    howmuchdata=len(data)
    for label in attr_vals_list[-1]:
        c=0
        for datum in data:
            if datum[index]==value and datum[-1]==label:
                c+=1
            if c==0 :
                continue
        else:
            subs+=(c/howmuchdata)*log(c/howmuchdata,2)
    subs*=-1
    #print(subs)
    return subs



def entropyhelperforithattribute(data,attr_vals_list,index,value):
    s=0
    #howmanyclass=len(classlist)
    subs=0
    attributevalues=attr_vals_list[index]
    for label in attr_vals_list[-1]:
        c=0
        howmuchdata=0
        for datum in data:
            if datum[index]==value and datum[-1]==label:
                c+=1
            if datum[index]==value:
                howmuchdata+=1
        #print("value",value,"label",label)
        #print("c",c,"datalen",howmuchdata)
        if c==0 or howmuchdata==0:
            continue
        else:
            subs+=(c/howmuchdata)*log(c/howmuchdata,2)
    subs*=-1
    #print(subs)
    return subs
            
            

def info_gain(data, attr_index, attr_vals_list):
    """
    Calculates the information gain on the current data when the attribute with attr_index is selected.
    :param data: Current data in the node
    :param attr_index: Selected attribute index to partition the data
    :param attr_vals_list: List of values that attributes may take
    :return: information gain (float), buckets (the list returned from divide)
    """
    dataentropy=entropy(data,attr_vals_list)
    #print(dataentropy)
    valuesthatattributecantake=attr_vals_list[attr_index]
    #print(valuesthatattributecantake)
    #print(data)
    #print(attr_index)
    howmuchdata=len(data)
    subs=0
    for i,label in enumerate(valuesthatattributecantake):
        #print(label)
        #print("here")
        c=0
        for datum in data:
    #        print(datum[attr_index],label)
            if datum[attr_index]==label:
                c+=1
        if c==0:
            #print("here for label",label)
            continue
        else:
            subs+=(c/howmuchdata)*entropyhelperforithattribute(data,attr_vals_list,attr_index,label)
    """if subs==0:
        print("f",attr_vals_list[attr_index])"""
    #print(dataentropy-subs)
    return [dataentropy-subs,divide(data,attr_index,attr_vals_list)]
    pass


def gain_ratio(data, attr_index, attr_vals_list):
    """
    Calculates the gain ratio on the current data when the attribute with attr_index is selected.
    :param data: Current data in the node
    :param attr_index: Selected attribute index to partition the data
    :param attr_vals_list: List of values that attributes may take
    :return: gain_ratio (float), buckets (the list returned from divide)
    """
    howmuchdata=len(data)
    valuesthatattributecantake=attr_vals_list[attr_index]
    gain=info_gain(data, attr_index, attr_vals_list)[0] #first element is gain
    subs=0
    for value in valuesthatattributecantake:
        c=0
        for datum in data:
            if datum[attr_index]==value:
                c+=1
        if c==0:
            continue
        else:
            subs+=(c/howmuchdata)*log(c/howmuchdata,2)
    subs*=-1
    if subs==0:
        return [0,divide(data,attr_index,attr_vals_list)]
    return [gain/subs,divide(data,attr_index,attr_vals_list)]
    pass


def gini(data, attr_vals_list):
    """
    Calculates the gini index in the current data.
    :param data: Current data in the node
    :param attr_vals_list: List of values that attributes may take
    (Last attribute is for the labels)
    :return: Calculated gini index (float)
    """
    s=0
    howmanyatt=len(attr_vals_list)-1
    totaldatalen=len(data)
    """for i in range(howmanyatt):
        setofvaluesthisattributecantake=attr_vals_list[i]
        #print(attr_vals_list[i])
        x=entropyhelperforithattribute(data,setofvaluesthisattributecantake,attr_vals_list[-1],i)
        print(x)"""
    subs=0
    howmuchdata=len(data)
    for label in attr_vals_list[-1]:
        c=0
        for datum in data:
            if datum[-1]==label:
                c+=1
        if c==0:
            continue
        else:
            subs+=(c/howmuchdata)**2
    subs=1-subs
    #print(subs)
    return subs 
    pass


def ginihelper(data,attr_vals_list,index,value):
    subs=0
    attributevalues=attr_vals_list[index]
    for label in attr_vals_list[-1]:
        c=0
        howmuchdata=0
        for datum in data:
            if datum[index]==value and datum[-1]==label:
                c+=1
            if datum[index]==value:
                howmuchdata+=1
        #print("value",value,"label",label)
        #print("c",c,"datalen",howmuchdata)
        if c==0 or howmuchdata==0:
            continue
        else:
            subs+=(c/howmuchdata)**2
    subs=1-subs
    #print(subs)
    return subs


def avg_gini_index(data, attr_index, attr_vals_list):
    """
    Calculates the average gini index on the current data when the attribute with attr_index is selected.
    :param data: Current data in the node
    :param attr_index: Selected attribute index to partition the data
    :param attr_vals_list: List of values that attributes may take
    :return: average gini index (float), buckets (the list returned from divide)
    """
    howmuchdata=len(data)
    valuesthatattributecantake=attr_vals_list[attr_index]
    #gini_si=gini(data[attr_index],attr_vals_list) #first element is gain
    subs=0
    for label in valuesthatattributecantake:
        c=0
        for datum in data:
            if datum[attr_index]==label:
                c+=1
        if c==0:
            continue
        else:
            subs+=(c/howmuchdata)*ginihelper(data,attr_vals_list,attr_index,label)
    
    return [subs,divide(data,attr_index,attr_vals_list)]
    pass
def calc_column(matris,index):
    howmanyrow=len(matris)
    s=0
    for i in range(howmanyrow):
        s+=matris[i][index]
    return s

def chi_squared_test(data, attr_index, attr_vals_list):
    """
    Calculated chi squared and degree of freedom between the selected attribute and the class attribute
    :param data: Current data in the node
    :param attr_index: Selected attribute index to partition the data
    :param attr_vals_list: List of values that attributes may take
    :return: chi squared value (float), degree of freedom (int)
    """
    attvaluelist=attr_vals_list[attr_index]
    x=len(attvaluelist)
    y=len(attr_vals_list[-1])
    matrix=[]
    r=0
    rowlist=[]
    for val in attvaluelist:
        forthisvalr=False
        for datum in data:
            if datum[attr_index]==val:
                forthisvalr=True
                rowlist.append(val)
                break
        if forthisvalr==True:
            r+=1
    
    c=0
    columnlist=[]
    for label in attr_vals_list[-1]:
        forthisvalc=False
        for datum in data:
            if datum[-1]==label and datum[attr_index] in attvaluelist:
                forthisvalc=True
                columnlist.append(label)
                break
        if forthisvalc==True:
            c+=1
    
    for i in range(r):
        matrix.append([])
        for j in range(c):
            matrix[i].append(0)
    #print(matrix)
    total=0
    for i,val in enumerate(rowlist):
        for j,label in enumerate(columnlist):
            counter=0
            for datum in data:
                if datum[attr_index]==val and datum[-1]==label:
                    counter+=1
            matrix[i][j]+=counter
            total+=counter
    exp=[]
    for i in range(r):
        exp.append([])
        for j in range(c):
            exp[i].append(0)
    for i in range(r):
        for j in range(c):
            rowval=sum(matrix[i])
            colval=calc_column(matrix,j)
            exp[i][j]=(rowval/total)*(colval/total)*total

    xobs2=0
    for i in range(r):
        for j in range(c):
            xobs2+=((matrix[i][j]-exp[i][j])**2)/exp[i][j]
    #print(xobs2)
    #print(matrix)
    #print(exp)
    #print(rowlist)
    #print(columnlist)
    #print(matrix)
    #print("r",r,"c",c)           
    #print("r,",len(attr_vals_list[-1]),"c",len(attvaluelist))
    return [xobs2,(r-1)*(c-1)]
    pass
