from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from url_input import URLInput
from scrape_url import ScrapeURL
from organize_data import OrganizeData
from export_excel import ExportExcel
import pandas as pd
import requests


# noinspection PyArgumentList
class StatsProUI(QMainWindow):
    def __init__(self, parent=None):
        super(StatsProUI, self).__init__(parent)
        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.setWindowTitle("StatsPro v1.0")
        self.setWindowIcon(QIcon('statspro.png'))
        self.screen = QDesktopWidget().screenGeometry()
        self.setGeometry(50, 50, self.screen.width()-100, self.screen.height()-100)
        self.setMaximumWidth(self.screen.width())
        self.setMaximumHeight(self.screen.height())
        self.layout = QGridLayout(self)
        self.central.setLayout(self.layout)
        self.scraper = None
        self.html_page = None
        self.organizer = None
        self.data_dict = {}
        self.excel_list = []
        self.url = ''

        self.welcome_msg = QMessageBox()
        self.welcome()
        self.valid_link = QMessageBox()
        self.invalid_link = QMessageBox()
        self.no_tables_msg = QMessageBox()

        self.input = QGroupBox("Enter a URL")
        self.in_layout = QVBoxLayout(self)
        self.input.setLayout(self.in_layout)
        self.input_button = QPushButton("Search")
        self.input_button.clicked.connect(self.handle_url)
        self.url_label = QLabel("Url: ")
        self.in_layout.addWidget(self.url_label)
        self.in_layout.setAlignment(Qt.AlignTop)
        self.url_line = QLineEdit(self)
        self.in_layout.addWidget(self.url_line)
        self.in_layout.addWidget(self.input_button)
        self.layout.addWidget(self.input, 1, 0)

        self.slogan = QLabel()
        self.slogan.setText("The Future of Data-Gathering.")
        self.font = QFont("Times", 14)
        self.font.setBold(True)
        self.font.setItalic(True)
        self.slogan.setFont(self.font)
        self.slogan.setStyleSheet("background-color: cyan")
        self.slogan.adjustSize()
        self.slogan.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.layout.addWidget(self.slogan, 2, 1)

        self.name_label = QLabel()
        self.name_label.setAlignment(Qt.AlignHCenter)
        self.name_label.setAlignment(Qt.AlignVCenter)
        self.name_label.adjustSize()
        self.name_label.setStyleSheet("background-color: cyan")
        self.pixmap = QPixmap("statspro.png")
        self.pixmap = self.pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.name_label.setPixmap(self.pixmap)
        self.layout.addWidget(self.name_label, 0, 0, 1, 0)

        self.past_urls = ''
        self.urls = QGroupBox("Past URLs:")
        self.url_layout = QVBoxLayout(self)
        self.url_layout.setAlignment(Qt.AlignTop)
        self.urls.setLayout(self.url_layout)
        self.url_label = QLabel("No URLs")
        self.url_label_font = QFont("Bahnschrift SemiBold", 7)
        self.url_label.setFont(self.url_label_font)
        self.url_label_font.setBold(True)
        self.in_layout.addWidget(self.url_label)

        self.data_box = QGroupBox("Data Preview")
        self.data_layout = QVBoxLayout(self)
        self.data_layout.setAlignment(Qt.AlignTop)
        self.data_box.setLayout(self.data_layout)
        self.data_label = QLabel("No Data")
        self.data_label.setWordWrap(True)
        self.data_label_font = QFont("Bahnschrift SemiBold", 7)
        self.data_label.setFont(self.data_label_font)
        self.data_label_font.setBold(True)
        self.data_layout.addWidget(self.data_label)
        self.layout.addWidget(self.data_box, 2, 0, 2, 1)

        self.saved_excels = ''
        self.excels = QGroupBox("Excel Files Created")
        self.excel_layout = QVBoxLayout(self)
        self.excel_layout.setAlignment(Qt.AlignTop)
        self.excels.setLayout(self.excel_layout)
        self.excel_label = QLabel("No Files Created")
        self.excel_label.setFont(self.url_label_font)
        self.excel_layout.addWidget(self.excel_label)
        self.layout.addWidget(self.excels, 1, 1)

    def welcome(self):
        self.welcome_msg.setWindowTitle("Welcome to StatPro!")
        self.welcome_msg.setText("Please enter your URL into the\ninput field and submit for results!")
        self.welcome_msg.setIcon(QMessageBox.Information)
        self.welcome_msg.exec()

    def invalid(self):
        self.invalid_link.setWindowTitle("Invalid Link")
        self.invalid_link.setText("Sorry, the URL provided was not valid!\n\nPlease enter another URL.")
        self.invalid_link.setIcon(QMessageBox.Critical)
        self.invalid_link.exec()

    def is_valid(self):
        self.valid_link.setWindowTitle("Valid Link")
        self.valid_link.setText("The URL provided has been searched!\n\nWould you like to export to Excel?")
        self.valid_link.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.valid_link.setIcon(QMessageBox.Information)
        reply = self.valid_link.exec()
        if reply == QMessageBox.Yes:
            self.export_xlsx()
        self.export_ui()

    def no_data(self):
        self.no_tables_msg.setWindowTitle("No Tables")
        self.no_tables_msg.setText("The URL provided has no data tables!\n\nPlease enter a different URL")
        self.no_tables_msg.setIcon(QMessageBox.Critical)
        self.no_tables_msg.setStandardButtons(QMessageBox.Close)
        self.no_tables_msg.exec()

    def handle_url(self):
        self.url = self.url_line.text()
        checker = URLInput(self.url)
        checker.check()
        if checker.get_valid():
            self.scraper = ScrapeURL(self.url)
            self.html_page = self.scraper.get_page()
            self.organizer = OrganizeData(self.html_page, self.url)
            self.organizer.organize()
            if not self.organizer.return_no_tables():
                if self.url not in self.data_dict.keys():
                    self.past_urls += self.url + '\n'
                    self.url_label.setText(str(self.past_urls))
                    self.is_valid()
            else:
                self.no_data()
        else:
            self.invalid()
        self.url_line.clear()

    def export_xlsx(self):
        exp = ExportExcel(self.url)
        exp.export_to_excel()
        filename = exp.get_filename()
        if filename not in self.excel_list:
            self.excel_list.append(filename)
            for file in filename:
                self.saved_excels += file + '\n'
        else:
            for file in filename:
                self.saved_excels += file + '\n'
        self.saved_excels += '\n'
        self.excel_label.setText(self.saved_excels)

    def export_ui(self):
        if not self.organizer.return_no_tables():
            pd.set_option('max_colwidth', 400)
            table = pd.read_html(requests.get(self.url).text)
            self.data_label.setText(table.to_string())
        else:
            self.no_tables()

