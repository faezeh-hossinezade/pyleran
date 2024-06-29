import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication,QMainWindow,QButtonGroup
from main_ui import Ui_MainWindow
from password_generator import PasswordGenerator

pwo = PasswordGenerator()

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        sttr_easy=  pwo.shuffle_password('0123456789', 8)
        self.easy_list=list(sttr_easy)
        sttr_hard= pwo.shuffle_password('0123456789abcdefghijklmnopqrstuvwxyz', 8)
        self.hard_list=list(sttr_hard)
        pwo.minlen = 8 # (Optional)
        pwo.maxlen = 8 # (Optional)
        pwo.minuchars = 2 # (Optional)
        pwo.minlchars = 3 # (Optional)
        pwo.minnumbers = 1 # (Optional)
        pwo.minschars = 1 # (Optional)
        sttr_diff=pwo.generate()
        self.difficult_list= list(sttr_diff)

        self.buttonGroup=QButtonGroup()
        self.buttonGroup.addButton(self.ui.radio_easy)
        self.buttonGroup.addButton(self.ui.radio_hard)
        self.buttonGroup.addButton(self.ui.radio_difficult)

        self.ui.radio_easy.toggled.connect(self.easy)
        self.ui.radio_hard.toggled.connect(self.hard)
        self.ui.radio_difficult.toggled.connect(self.difficult)

    def easy(self,check):
        if check:
            self.ui.btn_creat.clicked.connect(partial(self.x))
    
    def x(self):
        output=""
        random.shuffle(self.easy_list)
        for item in range(8):
            output+= self.easy_list[item]
        self.ui.text_box.setText(output)

    def hard(self,check):
        if check:
            self.ui.btn_creat.clicked.connect(partial(self.ejra))

    def ejra(self):
        output=""
        random.shuffle(self.hard_list)
        for item in range(8):
            output+= self.hard_list[item]
        self.ui.text_box.setText(output)

    def difficult(self,check):
        if check:
            self.ui.btn_creat.clicked.connect(partial(self.f))

    def f(self):
        output=""
        random.shuffle(self.difficult_list)
        for item in range(8):
            output+= self.difficult_list[item]
        self.ui.text_box.setText(output)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    main_window=Main_Window()
    main_window.show()
    app.exec()