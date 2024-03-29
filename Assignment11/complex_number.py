class Complex:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def add(self,other):
        totalx=self.x+other.x
        totaly=self.y+other.y
        print(f'Add Two Complex Numbers are equal = {totalx} + {totaly}*j')
    
    def sub(self,other):
        totalx=self.x-other.x
        totaly=self.y-other.y
        print(f'Sub Two Complex Numbers are equal = {totalx} - {totaly}*j')   
        
    def mul(self,other):
        totalx=self.x*other.x
        totaly=self.y*other.y
        print(f'Mul Two Complex Numbers are equal = {totalx} + {totaly}*j')    
        
        
num1=Complex(5,10)
num2=Complex(12,13)
num1.add(num2)
num1.sub(num2)
num1.mul(num2)
