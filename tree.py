import math
from node import Node

def majorClass(attributes, data, target):

    freq = {} #freq는 딕셔너리로 초기화
    index = attributes.index(target)#index는 attributes 내 타겟의 index

    #딕셔너리에 각각 값이 얼마나 있는지 저장
    for row in data:
        #if (freq.has_key(tuple[index])):
        if (row[index] in freq):
            freq[row[index]] += 1 
        else:
            freq[row[index]] = 1

    max_num = 0
    major = ""
    
    #값들 중 맥시멈 값 찾는 것(업데이트하는 형식)
    #딕셔너리의 최대값 찾고 키 찾는 다른 알고리즘
    for key in freq.keys():
        if freq[key]>max_num:
            max_num = freq[key]
            major = key

    return major

def info_gain(attributes, data, attr, targetAttr):
    
    freq = {}
    subsetEntropy = 0.0
    i = attributes.index(attr) #columns 들 중 선택된 column이 해당하는 인덱스
    y_idx = attributes.index(targetAttr)
    
    
    for entry in data: #한 줄 당 어떤 값이 몇 번 들어갔는지 dictionary에 카운트 
        #if (freq.has_key(entry[i])):
        if entry[i] in freq: # 한 줄에서 i번 째 값들을 통해 카운트
            freq[entry[i]] += 1.0
        else:
            freq[entry[i]]  = 1.0

    for val in freq.keys(): # 변수 내에 종류마다
        valProb        = freq[val] / sum(freq.values()) #이게 나올 확률
        dataSubset     = [entry for entry in data if entry[i] == val] 
        # 특정 변수의 종류를 가진 row만 선택해서 리스트에 넣음 
        subsetEntropy += valProb * myEntropy(get_col(y_idx,dataSubset))
        # 그것들 엔트로피 계산하고 합침
        
    return (myEntropy(get_col(y_idx,data)) - subsetEntropy)

def myEntropy(column_data):
    #column_data 는 리스트
    c = set(column_data)
    m = len(column_data)
    dataEntropy = 0.0
    
    for ci in c:
        p = column_data.count(ci)/m
        dataEntropy += (-p)*math.log2(p)
    return(dataEntropy)

def get_col(index,data):
    col = [data[m][index] for m,_ in enumerate(data)]
    return(col)

def get_cols(index,end,data):
    col = [data[m][index:end] for m,_ in enumerate(data)]
    return(col)

def my_attr_choose(data, attributes,target): 
    
    best = attributes[0] #best는 첫번째 attr 로 초기화
    maxGain = 0; #information gain 최고값 0으로 초기화
    y_idx = attributes.index(target)
    X_attributes = attributes[:y_idx]
    
    #column 돌면서 최대값 구하기
    for _,attr in enumerate(X_attributes):
        #col = get_col(i,data)
        newGain = info_gain(attributes, data, attr, target)
        if newGain>maxGain:
            maxGain = newGain
            best = attr
    #info gain 가장 높은것 반환
    return best


 
def get_data(data,attributes,attr,value):
    
    index = attributes.index(attr)
    
    new_data = []
    for row in data:
        if row[index] == value:
            new_data.append(row)
    
    return(new_data)

def build_tree(node,attributes,target):
    
    attributes = attributes.copy()
    data = node.data
    
    default = majorClass(attributes, data, target)
    target_idx = attributes.index(target)
    vals = get_col(target_idx,data)
    
    if not data or (len(attributes) - 1) <= 0: #data가 없거나 attributes가 없으면?
        return default #가장 많이나온 값 할당
    
    elif (len(set(vals))==1):    
        return vals[0] #똑같은 그 값 리턴
    
    else: 
    #재귀반복
        best = my_attr_choose(data,attributes,target)
        tree = {best:{}}
        index = attributes.index(best)
        value = set(get_col(index,data))
        
        for val in value:
             new_data = get_data(data,attributes,best,val)
             node.children.append(Node(new_data,best,val))
             
        for children in node.children:
            subtree = build_tree(children,attributes,target)
            tree[best][children.value] = subtree

    return tree
