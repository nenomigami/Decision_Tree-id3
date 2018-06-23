from tree import *
from node import *

class DecisionTree():
    
    def __init__(self):
        self.tree = {}

    def fit(self,training_set, attributes, target):
        data = Node(training_set,)
        self.tree = build_tree(data, attributes, target)
    
    def predict(self, test_set):
        test_set = test_set
        for row in test_set:
            tempDict = self.tree
            while(isinstance(tempDict, dict)):
                split = list(tempDict.keys())[0]
                tempDict = tempDict[split]
                
                index = attributes.index(split)
                row_value = row[index]
                tempDict = tempDict[row_value]
            row.append(tempDict)
        return(test_set)
            
if __name__ == "__main__":
        
    import numpy as np

    attributes = ["Outlook","Temp.","Humidity","Wind","Decision"]

    data = [["Sunny","Hot","High","Weak","No"],
            ["Sunny","Hot","High","Strong","No"],
            ["Overcast","Hot","High","Weak","Yes"],
            ["Rain","Mild","High","Weak","Yes"],
            ["Rain","Cool","Normal","Weak","Yes"],
            ["Rain","Cool","Normal","Strong","No"],
            ["Overcast","Cool","Normal","Strong","Yes"],
            ["Sunny","Mild","High","Weak","No"],
            ["Sunny","Cool","Normal","Weak","Yes"],
            ["Rain","Mild","Normal","Weak","Yes"],
            ["Sunny","Mild","Normal","Strong","Yes"],
            ["Overcast","Mild","High","Strong","Yes"],
            ["Overcast","Hot","Normal","Weak","Yes"],
            ["Sunny","Mild","High","Strong","No"]]

    test = [["Overcast","Hot","High","Weak","Yes"],
            ["Rain","Mild","High","Weak","Yes"],
            ["Rain","Cool","Normal","Weak","Yes"]]

    true1 = np.array([row[-1] for row in test])
    test1 = [row[:-1] for row in test]

    id3 = DecisionTree()
    id3.fit(data,attributes,"Decision")
    

    predict1 = id3.predict(test1)
    predict1 = np.array(get_col(-1,test1))
    print("accuracy : %0.2f" % (sum(true1 == predict1)/len(predict1)))
    print("following is bigger data\n\n")

    import csv
    with open('mushroom.csv','r') as file:
        reader = csv.reader(file,delimiter = ",")
        data = [row for row in reader]


    print("Data length: %s" %len(data))
    attributes = data[0]
    data.pop(0)

    id3 = DecisionTree()

    train_data = data[1:7000]
    test_data = data[7000:]

    true = [row[-1] for row in test_data]
    test_data = [row[:-1] for row in test_data]
    
    id3.fit(train_data,attributes,"edible")
    predict = id3.predict(test_data)
    predict = get_col(-1,test_data)

    true = np.array(true)
    predict = np.array(predict)
    
    print('accuracy is : %0.4f' %(sum(true == predict)/len(predict)))



