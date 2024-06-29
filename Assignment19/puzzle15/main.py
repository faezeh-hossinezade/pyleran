# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow
# from PySide6.QtCore import QFile
# from ui_mainwindow import Ui_MainWindow


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
        
        

# app = QApplication(sys.argv)
# untitled=MainWindow()
# untitled.show()
# app.exec()
import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox
from PySide6.QtCore import QFile
from puzzle15.ui_mainwindow import Ui_MainWindow
import random
from functools import partial
my_numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.buttons=[[self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4],
                      [self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btn_8],
                      [self.ui.btn_9, self.ui.btn_10, self.ui.btn_11,self.ui.btn_12],
                      [self.ui.btn_13,self.ui.btn_14,self.ui.btn_15,self.ui.btn_16]]

        for i in range(4):
            for j in range (4):
                # r=random.sample(range(1, 16), 1)
                num_rand=random.choice(my_numbers)
                self.buttons[i][j].setText(str(num_rand))
                self.buttons[i][j].clicked.connect(partial(self.play,i,j))
                my_numbers.remove(num_rand) 
                if num_rand==16:
                    # self.buttons[i][j].setText(" ")
                    self.buttons[i][j].setVisible(False)
                    self.empty_i=i
                    self.empty_j=j

    def play(self,i,j):
        if (i== self.empty_i and abs(j-self.empty_j)==1)\
            or (j== self.empty_j and abs(i-self.empty_i)==1):
                # print("bseco")
                self.buttons[self.empty_i][self.empty_j].setText(self.buttons[i][j].text()) 
                self.buttons[i][j].setText('16')
                self.buttons[self.empty_i][self.empty_j].setVisible(True) 
                self.buttons[i][j].setVisible(False)
                self.empty_i=i
                self.empty_j=j 
        if self.check_win == True:
                msg_box=QMessageBox()
                msg_box.setText("Barandeshodi Parande shodi :)")
                msg_box.exec_()
                
    def check_win(self):
        index=1
        for i in range(4):
            for j in range(4):
                if int(self.buttons[i][j].text())  !=index:
                    return False
                index+=1
        return True
            
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()