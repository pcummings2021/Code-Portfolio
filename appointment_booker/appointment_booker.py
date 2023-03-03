from PyQt5.QtWidgets import QMainWindow, QWidget, QCalendarWidget, QGridLayout, QGroupBox, QLabel, QHBoxLayout, \
    QComboBox, QPushButton, QLineEdit, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import *
from datetime import datetime, timedelta, date as d
from holiday_checker import HolidayChecker
from dateparser import parse


# noinspection PyArgumentList
class AppointmentBooker(QMainWindow):
    def __init__(self, parent=None):
        super(AppointmentBooker, self).__init__(parent)
        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.setWindowTitle("Dr. Parker's Appointment Booker")
        self.setGeometry(800, 100, 900, 900)
        self.layout = QGridLayout(self)
        self.central.setLayout(self.layout)
        self.dates_dict = dict()

        self.fall_check = HolidayChecker("https://www.fit.edu/registrar/academic-calendar/fall-2022/")
        self.spring_check = HolidayChecker("https://www.fit.edu/registrar/academic-calendar/spring-2023/")

        self.c = QCalendarWidget(self)
        self.calendar_box = QGroupBox("Calendar Preview")
        self.c_layout = QGridLayout()
        self.calendar_box.setLayout(self.c_layout)
        self.c.setMinimumDate(QDate.currentDate())
        self.c.setMaximumDate(QDate(2023, 5, 6))
        self.selected_date = self.c.selectedDate()
        self.c.selectionChanged.connect(self.check_date)
        self.c_layout.addWidget(self.c)
        self.layout.addWidget(self.calendar_box, 1, 0)
        self.holiday = ''

        self.date_box = QGroupBox(self)
        self.curr_date = self.selected_date.toString(Qt.SystemLocaleLongDate)
        self.date_label = QLabel(self.curr_date)
        self.date_label.setFont(QFont("Arial", 16))
        self.date_label.setStyleSheet("background-color: lightblue")
        self.date_layout = QGridLayout(self.date_label)
        self.date_box.setLayout(self.date_layout)
        self.date_layout.addWidget(self.date_label)
        self.layout.addWidget(self.date_box, 0, 0, 1, 4)

        self._book1 = QGroupBox("Book Single Appointment")
        self.book1_layout = QHBoxLayout(self)
        self._book1.setLayout(self.book1_layout)
        self.no_msg = QMessageBox()
        self.yes_msg = QMessageBox()
        self.t_msg = QMessageBox()

        self.hour = QComboBox(self)
        for i in range(1, 13):
            if i <= 9:
                self.hour.addItem("0" + str(i))
            else:
                self.hour.addItem(str(i))
        self.minute = QComboBox(self)
        for i in range(0, 60):
            if i <= 9:
                self.minute.addItem("0" + str(i))
            else:
                self.minute.addItem(str(i))
        self.meridian = QComboBox(self)
        self.meridian.addItems(["AM", "PM"])
        self.appt_length = QComboBox(self)
        self.appt_length.addItems(["10 mins", "15 mins", "20 mins", "25 mins", "30 mins"])
        self.book1_button = QPushButton("Book")
        self.book1_layout.addWidget(self.hour)
        self.book1_layout.addWidget(self.minute)
        self.book1_layout.addWidget(self.meridian)
        self.book1_layout.addWidget(self.appt_length)
        self.book1_layout.addWidget(self.book1_button)
        self.book1_button.clicked.connect(self.book_single)
        self.layout.addWidget(self._book1, 2, 0)

        self._book2 = QGroupBox("Book Multiple Appointments")
        self.book2_layout = QHBoxLayout(self)
        self._book2.setLayout(self.book2_layout)
        self.book2_button = QPushButton("Book")
        self.times = QLabel("Times: ")
        self.book2_layout.addWidget(self.times)
        self.book2_layout.addWidget(QLineEdit(self))
        self.book2_layout.addWidget(self.book2_button)
        self.book2_button.clicked.connect(self.book_multiple)
        self.layout.addWidget(self._book2, 3, 0)
        self.appt = ""
        self.today = parse(str(d.today()))
        self.book_multiple()

        self._current = QGroupBox("Current Bookings")
        self.curr_layout = QVBoxLayout(self)
        self.curr_layout.setAlignment(Qt.AlignTop)
        self._current.setLayout(self.curr_layout)
        self.curr_label = QLabel("No Current Bookings")
        self.curr_layout.addWidget(self.curr_label)
        self.curr_label.setText(self.appt)
        self.layout.addWidget(self._current, 1, 3, 4, 1)

    def book_single(self):
        hour = self.hour.currentText()
        minute = self.minute.currentText()
        meridian = self.meridian.currentText()
        temp = self.appt_length.currentText().index(" mins")
        appt_len = int(self.appt_length.currentText()[0:temp])
        day = self.selected_date.day()
        month = self.selected_date.month()
        year = self.selected_date.year()
        if int(day) <= 9:
            day = "0" + str(day)
        if int(month) <= 9:
            month = "0" + str(month)
        date = str(day) + str(month) + str(year)
        date = datetime.strptime(date, "%d%m%Y")
        appointment = str(hour) + str(minute) + str(meridian)
        appointment = datetime.strptime(appointment, "%I%M%p")
        self.appt = ""
        if not self.check_for_holiday(date):
            if date in self.dates_dict.keys() and self.check_overlap(date, appointment, appt_len):
                self.taken_message(appointment)
            else:
                if date not in self.dates_dict.keys():
                    self.dates_dict[date] = []
                    self.dates_dict[date].append([appointment, appt_len])
                    self.no_holiday_message()
                else:
                    self.dates_dict[date].append([appointment, appt_len])
                    self.no_holiday_message()

                for current in self.dates_dict[date]:
                    d1 = current[0]
                    leng = current[1]
                    d2 = d1 + timedelta(minutes=leng)
                    self.appt += self.time_string(d1) + ' - ' + self.time_string(d2) + ' ' + str(leng) + ' mins\n'
                self.curr_label.setText(self.appt)
        else:
            self.yes_holiday_message(self.holiday)

    def book_multiple(self):
        times = ["6:30am-7:00am", "7:00am-7:15am", "7:20am-7:30am", "8:00am-8:25am"]
        self.dates_dict[self.today] = []
        for t in times:
            # self.appt += t + '\n'
            t1 = t.split('-')
            start = parse(t1[0])
            end = parse(t1[1])
            dif = end-start
            leng = int(dif.seconds/60)
            start = start.replace(year=1900, month=1, day=1)
            end = end.replace(year=1900, month=1, day=1)
            self.appt += self.time_string(start) + " - " + self.time_string(end) + " " + str(leng) + " mins\n"
            self.dates_dict[self.today].append([start, leng])

    def check_date(self):
        self.selected_date = self.c.selectedDate()
        self.date_label.setText(self.selected_date.toString(Qt.SystemLocaleLongDate))
        month = str(self.selected_date.month())
        day = str(self.selected_date.day())
        year = str(self.selected_date.year())
        date_str = month + " " + day + " " + year
        date = datetime.strptime(date_str, "%m %d %Y")
        self.appt = ""
        if date in self.dates_dict.keys():
            for current in self.dates_dict[date]:
                d1 = current[0]
                leng = current[1]
                d2 = d1 + timedelta(minutes=leng)
                self.appt += self.time_string(d1) + ' - ' + self.time_string(d2) + ' ' + str(leng) + ' mins\n'
            self.curr_label.setText(self.appt)
        else:
            self.curr_label.setText("No Current Bookings")

    # noinspection PyMethodMayBeStatic
    def time_string(self, date):
        h = date.hour
        m = date.minute
        h_s = ''
        m_s = ''
        meridian = ' '
        if h <= 9:
            h_s += "0" + str(h)
        else:
            h_s = str(h)
        if m <= 9:
            m_s += "0" + str(m)
        else:
            m_s = str(m)
        if h >= 12:
            meridian += "pm"
        else:
            meridian += "am"
        time_str = str(h_s) + ":" + str(m_s) + str(meridian)
        return time_str

    def check_for_holiday(self, date):
        fall = self.fall_check.is_holiday(date)
        spring = self.spring_check.is_holiday(date)
        if fall or spring:
            if fall and not spring:
                self.holiday = self.fall_check.get_holiday_desc(date)
            if spring and not fall:
                self.holiday = self.spring_check.get_holiday_desc(date)
            return True
        return False

    def no_holiday_message(self):
        self.no_msg.setWindowTitle("Appointment Booked")
        self.no_msg.setText("Your Appointment has been booked!")
        self.no_msg.setIcon(QMessageBox.Information)
        self.no_msg.setStandardButtons(QMessageBox.Close)
        self.no_msg.exec()

    def yes_holiday_message(self, holiday):
        self.yes_msg.setWindowTitle("Holiday :)")
        self.yes_msg.setText("Sorry, the date selected is a Holiday, " + holiday +
                             " so an appointment cannot be booked.")
        self.yes_msg.setIcon(QMessageBox.Critical)
        self.yes_msg.setStandardButtons(QMessageBox.Close)
        self.yes_msg.exec()

    def taken_message(self, appointment):
        appt = self.time_string(appointment)
        self.t_msg.setWindowTitle("Appointment Filled")
        self.t_msg.setText("Sorry, Dr. Parker already has an appointment booked at " + appt)
        self.t_msg.setIcon(QMessageBox.Critical)
        self.t_msg.setStandardButtons(QMessageBox.Close)
        self.t_msg.exec()

    def check_overlap(self, date, appointment, appt_len):
        for i in self.dates_dict[date]:
            st1 = i[0]
            en1 = i[0] + timedelta(minutes=i[1])
            st2 = appointment
            en2 = appointment + timedelta(minutes=appt_len)
            if st1 < en2 and st2 < en1:
                return True
        return False
