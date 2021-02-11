# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sorting
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(425, 40, 171, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.button_generate = QtWidgets.QPushButton(self.centralwidget)
        self.button_generate.setGeometry(QtCore.QRect(240, 40, 171, 41))
        self.button_generate.setObjectName("button_generate")

        self.button_animate = QtWidgets.QPushButton(self.centralwidget)
        self.button_animate.setGeometry(QtCore.QRect(610, 40, 171, 41))
        self.button_animate.setObjectName("button_animate")
        # connect button to functionality
        self.button_animate.clicked.connect(self.choose_algo)
        self.button_generate.clicked.connect(self.generate_array)

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(70, 60, 160, 16))
        self.horizontalSlider.setMinimum(2)
        self.horizontalSlider.setMaximum(120)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 780, 460))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # create graphics scene and add to the layout (position predefined by vertical layout widget
        self.scene = QtWidgets.QGraphicsScene()
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.verticalLayout.addWidget(self.view)
        self.view.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(45, 45, 45)))
        # align coordinate system so that (0, 0) is in upper left corner
        self.view.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.scene_width = 780
        self.scene_height = 360
        # create array
        self.array = sorting.get_random_array(2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Sorting Visualizer using PyQt5"))
        self.comboBox.setItemText(0, _translate("MainWindow", "BubbleSort"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Insertion Sort"))
        self.button_animate.setText(_translate("MainWindow", "Animate!"))
        self.button_generate.setText(_translate("MainWindow", "Generate"))
        self.label.setText(_translate("MainWindow", "Adjust Array Size"))

    # generates a random array of specified size
    def get_random_array(self, size):
        array = []
        for i in range(0, size):
            array.append(randint(5, 400))

        return array

    # executed when button_generate is clicked:
    # builds a new array of specified size and displays it in GUI
    def generate_array(self):
        size = self.horizontalSlider.value()
        self.array = self.get_random_array(size)
        self.scene.clear()
        self.add_rects()

    # add rectangles if button was clicked
    def add_rects(self):
        w1 = int(self.scene_width // len(self.array))
        for i in range(0, len(self.array)):
            rect = QtWidgets.QGraphicsRectItem(i*w1, 0, w1, self.array[i])
            rect.setBrush(QtGui.QBrush(QtGui.QColor(127, 255, 212)))
            self.scene.addItem(rect)

    def update_rects(self, pos1, pos2, finished):
        self.scene.clear()
        w1 = int(self.scene_width // len(self.array))
        rect_list = []
        for i in range(0, len(self.array)):
            rect = QtWidgets.QGraphicsRectItem(i * w1, 0, w1, self.array[i])
            if i == pos1 or i == pos2:
                rect.setBrush(QtGui.QBrush(QtGui.QColor(255, 64, 64)))
            elif i >= finished:
                rect.setBrush(QtGui.QBrush(QtGui.QColor(0, 255, 0)))
            else:
                rect.setBrush(QtGui.QBrush(QtGui.QColor(127, 255, 212)))
            self.scene.addItem(rect)
            rect_list.append(rect)

    def choose_algo(self):
        if len(self.array) < 10:
            speed = 300
        else:
            speed = 120 - len(self.array)

        self.button_animate.setEnabled(False)
        self.button_generate.setEnabled(False)

        if self.comboBox.currentText() == "BubbleSort":
            self.bubble_sort(speed)
        else:
            pass

        self.button_animate.setEnabled(True)
        self.button_generate.setEnabled(True)

    def bubble_sort(self, speed):
        swapped = True
        for i in range(0, len(self.array)):
            if not swapped:
                self.update_rects(-1, -1, -1)
                break
            swapped = False
            for j in range(0, len(self.array) - i - 1):
                self.update_rects(j, j+1, len(self.array) - i)
                if self.array[j] > self.array[j + 1]:
                    self.update_rects(j, j+1, len(self.array)-i)
                    temp = self.array[j]
                    self.array[j] = self.array[j + 1]
                    self.array[j + 1] = temp
                    QtTest.QTest.qWait(speed)
                    swapped = True
            self.update_rects(0, 0, len(self.array)-i)
        return self.array



