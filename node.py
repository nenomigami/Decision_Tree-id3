class Node():
    
    def __init__(self,data,attribute = "",value = ""):
        self.children = [] #children 리스트 초기화
        self.data = data
        self.attribute = attribute
        self.value = value
        self.criterion = attribute + " = " + value
