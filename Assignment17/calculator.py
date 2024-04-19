from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from functools import partial
import math


#QuiLoader=class
# one app
# some winows

myapp=QApplication([])
loader=QUiLoader()
mywindow=loader.load("calculator.ui")
#mywindow is object
mywindow.show()
# def test():
#     a=int(mywindow.lineEdit.setText("Tada!"))
#     mywindow.txtbox.setText("")


# 1- show numbers , 2- clear box:
def num(x):
    num = mywindow.box.text()  
    mywindow.box.setText(num + x)
    
    
    
def sum():
    global num1 , num2 , outcome
    global operator
    operator = "+"
    num1 = mywindow.box.text()
    mywindow.box.setText("")
    ### clear box afre entering number
    
def sub():
    global num1, num2 , outcome 
    global operator
    operator = str("-")
    num1 = mywindow.box.text()
    mywindow.box.setText("")    
    
    
def mult():
    global num1, num2 , outcome
    global operator
    operator = "x"
    num1 = mywindow.box.text()
    mywindow.box.setText("")
    
def divide():
    global num1, num2 ,outcome
    global operator
    operator = "÷"
    num1 = mywindow.box.text()
    mywindow.box.setText("")

def ac():
    mywindow.box.setText("")
    


def percent():
    global num1, num2 , outcome, num3
    global operator
    # operator = str("%")
    operator = "%"
    num1 = mywindow.box.text()
    num3=float(num1)
    mywindow.box.setText("")    
    # num2=float(num1)
    # num2/= float(100)
    # mywindow.box.setText("")   
    # mywindow.box.setText(str(num2)) 
    
    
def sqrt():
    global num1, outcome
    global operator
    operator= "√"
    num1 = mywindow.box.text()
    if float(num1)<0:
        mywindow.box.setText("ERROR")
    else:
        outcome = math.sqrt(float(num1))
        mywindow.box.setText(str(outcome))
        
        
def plus_minus():
    global num1 , operator
    operator="+/-"
    num1 = float(mywindow.box.text())
    mywindow.box.setText("")
    outcome =float(num1)*-1
    mywindow.box.setText(str(outcome))
    
    
def sinus():
    global num1, outcome
    global operator
    operator = "sin"
    num1 = mywindow.box.text()
    outcome = math.sin(math.radians(float(num1)))
    mywindow.box.setText(str(outcome))
    
def cosinus():
    global num1, outcome
    global operator
    operator = "cos"
    num1 = mywindow.box.text()
    outcome = math.cos(math.radians(float(num1)))
    mywindow.box.setText(str(outcome))

def tanjant():
    global num1, outcome
    global operator
    operator = "tan"
    num1 = mywindow.box.text()
    outcome = math.tan(math.radians(float(num1)))
    mywindow.box.setText(str(outcome))

def log():
    global num1, outcome
    global operator
    operator = "log"
    num1 = mywindow.box.text()
    if float(num1)>0:
        outcome = math.log(int(num1))
        mywindow.box.setText(str(outcome))
    else:
        mywindow.box.setText("ERROR")
    
    
def cotanjant():
    global num1, outcome
    global operator
    operator = "cot"
    num1 = mywindow.box.text()
    if math.tan(math.radians(float(num1)))==0:
        mywindow.box.setText("ERROR")
    else:
        outcome = 1/math.tan(math.radians(float(num1)))
        mywindow.box.setText(str(outcome))

    
def result(outcome):
    if operator == "-" :
            num2 = mywindow.box.text()
            outcome = float(num1) - float(num2)
            mywindow.box.setText(str(outcome))
            
    elif operator == "%":
        num2=float(100.0)
        
        outcome = num3/num2
        
        mywindow.box.setText(str(outcome))
            
    elif operator == "+" :
        num2 = mywindow.box.text()
        outcome = float(num1) + float(num2)
        mywindow.box.setText(str(outcome))
        
    elif operator == "x" :
        num2 = mywindow.box.text()
        outcome = float(num1) * float(num2)
        mywindow.box.setText(str(outcome))

    elif operator == "÷" :
        num2 = mywindow.box.text()
        if num2 == 0 :
            mywindow.box.setText("ERROR")            
        else:
            outcome = float(num1) / float(num2)
            mywindow.box.setText(str(outcome)) 
    
    # elif operator=="+/-":
    #     num1= mywindow.box.text()
    #     outcome =float(num1)*-1
    #     mywindow.box.setText(str(outcome))
        



# Numbers:
mywindow.btn_0.clicked.connect(partial(num, "0"))
mywindow.btn_1.clicked.connect(partial(num, "1"))
mywindow.btn_2.clicked.connect(partial(num, "2"))
mywindow.btn_3.clicked.connect(partial(num, "3"))
mywindow.btn_4.clicked.connect(partial(num, "4"))
mywindow.btn_5.clicked.connect(partial(num, "5"))
mywindow.btn_6.clicked.connect(partial(num, "6"))
mywindow.btn_7.clicked.connect(partial(num, "7"))
mywindow.btn_8.clicked.connect(partial(num, "8"))
mywindow.btn_9.clicked.connect(partial(num, "9"))
mywindow.btn_dot.clicked.connect(partial(num, "."))



# operators:
mywindow.sub.clicked.connect(sub)
mywindow.percent.clicked.connect(sub)
mywindow.sum.clicked.connect(sum)
mywindow.power.clicked.connect(mult)
mywindow.divide.clicked.connect(divide)
mywindow.plus_minus.clicked.connect(plus_minus)
mywindow.percent.clicked.connect(percent)
mywindow.sqrt.clicked.connect(sqrt)
mywindow.sinus.clicked.connect(sinus)
mywindow.cosinus.clicked.connect(cosinus)
mywindow.tanjant.clicked.connect(tanjant)
mywindow.cotanjant.clicked.connect(cotanjant)
mywindow.clear.clicked.connect(ac)



# basic operators
mywindow.equal.clicked.connect(result)



myapp.exec()