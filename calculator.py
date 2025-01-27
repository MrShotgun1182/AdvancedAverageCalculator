class Calculator: 
    data = []
    average = 0

    def __init__(self,data):
        self.data = data

    def add(self,data):
        self.data.append(data)

    def remove(self,name):
        for data in self.data: 
            if(data['name'] == name):
                self.data.remove(data)
    
    def calculate(self):
        totalScore = 0
        totalCoefficient = 0
        for data in self.data: 
            totalCoefficient += int(data['coefficient'])
            totalScore += data['score'] * data['coefficient']
        
        try: 
            self.average = totalScore / totalCoefficient
            return self.average
        except: 
            return 0
