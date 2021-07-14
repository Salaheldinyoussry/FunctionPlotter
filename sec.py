import sys
import numpy as np
import  numexpr
from PySide2.QtGui import QIcon, QFont, QPalette, QColor
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGroupBox, QGridLayout, QLineEdit, \
    QLabel, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from decimal import Decimal


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.X = [0]
        self.Y = [0]
        self.setWindowTitle("Equation plotter")
        self.setGeometry(500, 100, 1000, 800)

        self.setIcon()

        self.createGridLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(250, 250, 250))
        self.setPalette(palette)
        self.setAutoFillBackground(True)


        self.show()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def say_hello(self):
        try:
            s=int(str(self.text1.text()))
            e = int(str(self.text2.text()))
            eqn=self.text.text()
            eqn=eqn.replace("^","**")
            eqn=eqn.replace("e","2.718")


           ###
            self.X=np.arange(s, e, step=0.1)
            x=self.X
            X=self.X
            self.Y=numexpr.evaluate(eqn)
            ###
            # self.X = [0, 1, 2, 3, 4]
            # self.Y = [10, 10, 10, 10, 40]
            self.sc = MplCanvas(self, width=5, height=4, dpi=100)
            self.sc.axes.plot(self.X, self.Y)
            self.gridLayout.addWidget(self.sc, 4, 0, 1, 4)
        except:
            #userInfo = QMessageBox.question(self, "enter a valid eqn (as x*3 +2 ) and  range")
            userInfo = QMessageBox.about(self, "error", "enter a valid eqn (as x*3 +2 ) and a valid integer range   ",
                                )

    def createGridLayout(self):
        self.groupBox = QGroupBox()
        self.groupBox.setFont(QFont("Sanserif", 13))
        self.gridLayout = QGridLayout()

        self.label = QLabel("eqn")
        self.gridLayout.addWidget(self.label, 0, 0)
        self.text = QLineEdit( self)
        self.gridLayout.addWidget(self.text, 0, 1,1,3)

        self.label1 = QLabel("min")
        self.gridLayout.addWidget(self.label1, 1, 0,1,1)
        self.text1 = QLineEdit(self)
        self. gridLayout.addWidget(self.text1, 1, 1,1,1)

        self.label2 = QLabel("max")
        self.gridLayout.addWidget(self.label2, 1,2,1,1)
        self.text2 = QLineEdit(self)
        self.gridLayout.addWidget(self.text2, 1, 3,1,1)

        button1 = QPushButton("plot ", self)
       # button1.setIcon(QIcon("css.png"))
        button1.clicked.connect(self.say_hello)
        self.gridLayout.addWidget(button1, 2, 1)

        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.sc.axes.plot(self.X, self.Y)
        self.gridLayout.addWidget(self.sc,4,0,1,4 )

        # button2 = QPushButton("javascript", self)
        # button2.setIcon(QIcon("javascript.png"))
        # gridLayout.addWidget(button2, 1, 0)
        #
        # button3 = QPushButton("C#", self)
        # button3.setIcon(QIcon("csharp.png"))
        # gridLayout.addWidget(button3, 1, 1)
        #
        # button4 = QPushButton("Python", self)
        # button4.setIcon(QIcon("pythonicon.png"))
        # gridLayout.addWidget(button4, 2, 0)
        #
        # button5 = QPushButton("Java", self)
        # button5.setIcon(QIcon("java.png"))
        # gridLayout.addWidget(button5, 2, 1)

        self.groupBox.setLayout(self.gridLayout)


myapp = QApplication(sys.argv)
window = Window()

myapp.exec_()
sys.exit()