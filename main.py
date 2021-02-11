import sorting
import sys
from PyQt5 import QtCore, QtWidgets
from ui.mainwindow import Ui_MainWindow


if __name__ == '__main__':
    # create array
    array = sorting.get_random_array(50)
    # use GUI
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.setWindowTitle("Sorting Visualizer")

    ui_window = Ui_MainWindow()
    ui_window.setupUi(window)

    window.show()
    sys.exit(app.exec_())