class Calculator: 
    data = []

    def __init__(self,data):
        self.data = data

    def add(self,data):
        self.data.append(data)

    def remove(self,name):
        for data in self.data: 
            if(data['name'] == name):
                self.data.remove(data)
    
