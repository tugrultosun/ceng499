from dt import divide, entropy, info_gain, gain_ratio, gini, avg_gini_index, chi_squared_test
from statistics import mode
import pickle
import pprint
from graphviz import Digraph
from scipy.stats import chi2
with open('hw3_data/dt/data.pkl','rb') as f:
    train_data, test_data, attr_vals_list, attr_names = pickle.load(f)

#print(attr_vals_list[-1])
#print(attr_names)
#print(train_data[0])
#print(attr_names)
#print(entropy(train_data,attr_vals_list))
#print(attr_vals_list)
def gainratioattributefinder(data,attr_vals,targetattribute):
    howmanyatt=len(attr_vals)
    d=d=attr_vals+[targetattribute]
    gainratiolist=[]
    for i in range(howmanyatt):
        gainratiolist.append(gain_ratio(data,i,d)[0])
    c=gainratiolist.index(max(gainratiolist))
    #print(gainratiolist)
    return c
def informationgainattributefinder(data,attr_vals,targetattribute):
    howmanyatt=len(attr_vals)
    d=attr_vals+[targetattribute]
    #print(c)
    #print(attr_vals)
    gainratiolist=[]
    for i in range(howmanyatt):
        gainratiolist.append(info_gain(data,i,d)[0])
    c=gainratiolist.index(max(gainratiolist))
    #print(gainratiolist)
    #print(attr_vals[c])
    #printer(data)
    return c
def avgginiindexattributefinder(data,attr_vals,targetattribute):
    howmanyatt=len(attr_vals)
    d=attr_vals+[targetattribute]
    gainratiolist=[]
    for i in range(howmanyatt):
        gainratiolist.append(avg_gini_index(data,i,d)[0])
    c=gainratiolist.index(min(gainratiolist))
    return c
def doesbelongsameclass(data):
    labels=[]
    for datum in data:
        labels.append(datum[-1])
    belong=(len(set(labels))==1)
    return belong
def belongwhichclass(data):
    labels=[]
    for datum in data:
        labels.append(datum[-1])
    
    return labels[0]

def mostcommon(data):
    classlabellist=[]
    for datum in data:
        classlabellist.append(datum[-1])
    #print("unacc",classlabellist.count("unacc"))
    #print("acc",classlabellist.count("acc"))
    return mode(classlabellist)
def printer(data):
    classlabellist=[]
    for datum in data:
        classlabellist.append(datum[-1])
    unacc=classlabellist.count("unacc")
    acc=classlabellist.count("acc")
    return [unacc,acc]
def subattributes(attributes,index):
    copiedattributes=[]
    for att in attributes:
        copiedattributes.append(att)
    copiedattributes.pop(index)
    #attributes.pop(index)
    return copiedattributes
def subnames(names,index):
    copiednames=[]
    for name in names:
        copiednames.append(name)
    copiednames.pop(index)
    #attributes.pop(index)
    return copiednames
def mostcommonv2(data,vi,i):
    classlabellist=[]
    for datum in data:
        if datum[i]==vi:
            classlabellist.append(datum[-1])
    #print("unacc",classlabellist.count("unacc"))
    #print("acc",classlabellist.count("acc"))
    return mode(classlabellist)
def id3withinfogain(data,targetattribute,attributes,attr_name,toti):
    #print(attr_names)
    #print("call made")
    root={}
    #print(data)
    #for i in range(len(attributes)):
    #    print(len(divide(data,i,attributes)))
    #print(len(divide(data,3,attributes)))
    #print(targetattribute)
    #print(attributes)
    if doesbelongsameclass(data):
        #print("here")
        return belongwhichclass(data)
    if len(attributes)==0:
        #print("here2")
        return mostcommon(data)
    else:
        attributeindex=informationgainattributefinder(data,toti,targetattribute)
        #print(attributes)
        dadi=subattributes(toti,attributeindex)
        #print(toti[attributeindex])
        atn=attr_name[attributeindex]
        #print(attr_names)
        #print(atn)
        #attr_names.pop(attributeindex)
        root[atn]={}
        abc=toti[attributeindex]
        test=divide(data,attributeindex,toti)
        
        #attributes.pop(attributeindex)
        
        #print(abc)
        for i,vi in enumerate(abc):
            #print(i,vi,attributes.index(toti[attributeindex]))
            #print(vi,atn)
            root[atn][vi]=None 
            if(len(test[i])==0):
                #print("here4",abc)
                root[atn][vi]=mostcommon(data)
                #attributes.pop(attributeindex)
            else:
                #print(test[i])
                #print(subattributes(attributes,attributeindex))
                #attributes.pop(attributeindex)
                #print("dadidadi")
                root[atn][vi]=id3withinfogain(test[i],targetattribute,dadi,attr_name,toti)
                #return id33(test,targetattribute,attributes)
    return root

def id3withgainratio(data,targetattribute,attributes,attr_name,toti):
    #print(attr_names)
    #print("call made")
    root={}
    #print(data)
    #for i in range(len(attributes)):
    #    print(len(divide(data,i,attributes)))
    #print(len(divide(data,3,attributes)))
    #print(targetattribute)
    #print(attributes)
    if doesbelongsameclass(data):
        #print("here")
        return belongwhichclass(data)
    if len(attributes)==0:
        #print("here2")
        return mostcommon(data)
    else:
        attributeindex=gainratioattributefinder(data,toti,targetattribute)
        #print(attributes)
        dadi=subattributes(toti,attributeindex)
        #print(toti[attributeindex])
        atn=attr_name[attributeindex]
        #print(attr_names)
        #print(atn)
        #attr_names.pop(attributeindex)
        root[atn]={}
        abc=toti[attributeindex]
        test=divide(data,attributeindex,toti)
        
        #attributes.pop(attributeindex)
        
        #print(abc)
        for i,vi in enumerate(abc):
            #print(i,vi,attributes.index(toti[attributeindex]))
            #print(vi,atn)
            root[atn][vi]=None 
            if(len(test[i])==0):
                #print("here4",abc)
                root[atn][vi]=mostcommon(data)
                #attributes.pop(attributeindex)
            else:
                #print(test[i])
                #print(subattributes(attributes,attributeindex))
                #attributes.pop(attributeindex)
                #print("dadidadi")
                root[atn][vi]=id3withgainratio(test[i],targetattribute,dadi,attr_name,toti)
                #return id33(test,targetattribute,attributes)
    return root
def id3withavgginiindex(data,targetattribute,attributes,attr_name,toti):
    #print(attr_names)
    #print("call made")
    root={}
    #print(data)
    #for i in range(len(attributes)):
    #    print(len(divide(data,i,attributes)))
    #print(len(divide(data,3,attributes)))
    #print(targetattribute)
    #print(attributes)
    if doesbelongsameclass(data):
        #print("here")
        return belongwhichclass(data)
    if len(attributes)==0:
        #print("here2")
        return mostcommon(data)
    else:
        attributeindex=avgginiindexattributefinder(data,toti,targetattribute)
        #print(attributes)
        dadi=subattributes(toti,attributeindex)
        #print(toti[attributeindex])
        atn=attr_name[attributeindex]
        #print(attr_names)
        #print(atn)
        #attr_names.pop(attributeindex)
        root[atn]={}
        abc=toti[attributeindex]
        test=divide(data,attributeindex,toti)
        
        #attributes.pop(attributeindex)
        
        #print(abc)
        for i,vi in enumerate(abc):
            #print(i,vi,attributes.index(toti[attributeindex]))
            #print(vi,atn)
            root[atn][vi]=None 
            if(len(test[i])==0):
                #print("here4",abc)
                root[atn][vi]=mostcommon(data)
                #attributes.pop(attributeindex)
            else:
                #print(test[i])
                #print(subattributes(attributes,attributeindex))
                #attributes.pop(attributeindex)
                #print("dadidadi")
                root[atn][vi]=id3withavgginiindex(test[i],targetattribute,dadi,attr_name,toti)
                #return id33(test,targetattribute,attributes)
    return root
def id3withgainratiopreprun(data,targetattribute,attributes,attr_name,toti):
    #print(attr_names)
    #print("call made")
    root={}
    #print(data)
    #for i in range(len(attributes)):
    #    print(len(divide(data,i,attributes)))
    #print(len(divide(data,3,attributes)))
    #print(targetattribute)
    #print(attributes)
    if doesbelongsameclass(data):
        #print("here")
        return belongwhichclass(data)
    if len(attributes)==0:
        #print("here2")
        return mostcommon(data)
    else:
        attributeindex=gainratioattributefinder(data,toti,targetattribute)
        #print(attributes)
        dadi=subattributes(toti,attributeindex)
        #print(toti[attributeindex])
        atn=attr_name[attributeindex]
        #print(attr_names)
        #print(atn)
        #attr_names.pop(attributeindex)
        root[atn]={}
        abc=toti[attributeindex]
        test=divide(data,attributeindex,toti)
        
        #attributes.pop(attributeindex)
        prob=0.90
        chisq=chi_squared_test(data, attributeindex, toti+[targetattribute])
        dof=chisq[1]
        xobs2=chisq[0]
        critical=chi2.ppf(prob,dof)
        #print(critical)
        #print(abc)
        if abs(xobs2)<=critical:
            return mostcommon(data)
        for i,vi in enumerate(abc):
            #print(i,vi,attributes.index(toti[attributeindex]))
            #print(vi,atn)
            root[atn][vi]=None
            
            if(len(test[i])==0):
                #print("here4",abc)
                root[atn][vi]=mostcommon(data)
                #attributes.pop(attributeindex)
            else:
                #print(test[i])
                #print(subattributes(attributes,attributeindex))
                #attributes.pop(attributeindex)
                #print("dadidadi")
                root[atn][vi]=id3withgainratiopreprun(test[i],targetattribute,dadi,attr_name,toti)
                #return id33(test,targetattribute,attributes)
    return root

def testerhelper(datum,tree,attr_names):
    #print(tree)
    if tree=='unacc':
        return tree
    if tree=='acc':
        return tree
    #print("falled")
    for key in tree.keys():
        #print(key)
        keyindex=attr_names.index(key)
        #print(keyindex)
        for value in tree[key].keys():
            #print(value)
            if datum[keyindex]==value:
                #print("here2")
                returnedthing=testerhelper(datum,tree[key][value],attr_names)
    return returnedthing
    
def tester(test_data,tree,attr_names):
    #print(test_data)
    totaltestcounter=0
    correcttestcounter=0
    for datum in test_data:
        totaltestcounter+=1
        valuepredicted=testerhelper(datum,tree,attr_names)
        #print(valuepredicted)
        actualvalue=datum[-1]
        if valuepredicted==actualvalue:
            correcttestcounter+=1
    return correcttestcounter/totaltestcounter
    
        
    


  

def print_tree(node, dot,indices,current_index):
    if type(node)==str:
        return  # since we create the node and edge in the upper sections, we don't need to do anything
    for key in node.keys():
        for value in node[key].keys():
            
            child_index=indices[-1]+1
            indices.append(child_index)
            if node[key][value]=='acc' or node[key][value]=='unacc':
                dot.node(str(child_index), str(node[key][value]))
            else:
                for value2 in node[key][value].keys():
                    #print(key,value,value2)
                    dot.node(str(child_index), value2)
            
            dot.edge(str(current_index),str(child_index),value )
         # increment the last index in the list and assign it to the child node
          # appending will modify the very same list so we are telling that we have already used that index
          # create the node for the child
         # create an edge labeled with the value of the selected attribute
            print_tree(node[key][value], dot,indices,child_index)  # recursively continue to create the tree



tree=id3withgainratiopreprun(train_data,attr_vals_list[-1],attr_vals_list[:-1],attr_names,attr_vals_list[:-1])
dot = Digraph()  # instantiate the graph# the first parameter is the name which should be a unique identifier, the second one is the label
# normally the label is the first argument by default but the same node name may occur in different branches of the tree so I wanted to separate the label and its unique id.
dot.node('1', list(tree.keys())[0])
print_tree(tree, dot,[1],1)  # recursively create the tree initialized the indices list with [1] since the unique id of our already created root node is 1.
dot.render("gainratiopreprun", view=True)  # if view==True it opens it


print("Test accuracy for gainratiopreprun is ",tester(test_data,tree,attr_names))

