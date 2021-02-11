import sys
from PyQt5 import QtCore, QtWidgets
from ui.mainwindow import Ui_MainWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui_window = Ui_MainWindow()
    ui_window.setupUi(window)
    window.show()
    sys.exit(app.exec_())