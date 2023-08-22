class CALC_BMI:
    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
   
    def get_name(self):
        return self.name
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight
    
    def formula(self):
        h = self.height
        w = self.weight
        f1 = h/100
        f2 =  f1*f1
        f3 = w/f2
        return f3
    