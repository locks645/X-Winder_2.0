import sys, time
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from test_gui_1_code import Ui_main_window

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mw = Ui_main_window()
        self.mw.setupUi(self)
        self.init_widgets()

    def init_widgets(self):
        self.mw.pb_initialization.clicked.connect(self.init_clicked)
        self.mw.pb_calculations.clicked.connect(self.calc_clicked)
        self.mw.pb_hoop_forwards.clicked.connect(self.hoopf_clicked)
        self.mw.pb_hoop_backwards.clicked.connect(self.hoopb_clicked)
        self.mw.pb_helical_forwards.clicked.connect(self.helif_clicked)
        self.mw.pb_helical_backwards.clicked.connect(self.helib_clicked)

    def init_clicked(self):
        print('init finished')
    
    def calc_clicked(self):
        print('calc finished')

    def hoopf_clicked(self):
        print('hoopf finished')

    def hoopb_clicked(self):
        print('hoopb finished')

    def helif_clicked(self):
        print('helif finished')

    def helib_clicked(self):
        print('helib finished')


def main():
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    win = main_window()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()