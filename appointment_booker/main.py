from appointment_booker import AppointmentBooker
from PyQt5.QtWidgets import *
import sys


def main():
    app = QApplication(sys.argv)
    booker = AppointmentBooker()
    booker.show()
    sys.exit(app.exec())


main()
