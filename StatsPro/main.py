from statspro_ui import StatsProUI
from PyQt5.QtWidgets import *
import sys


def main():
    app = QApplication(sys.argv)
    statpro_ui = StatsProUI()
    statpro_ui.show()
    sys.exit(app.exec())


main()
