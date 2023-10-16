import pandas as pd
import requests


class ExportExcel:
    def __init__(self, url):
        self.url = url
        self.filename = []

    def export_to_excel(self):
        table = pd.read_html(requests.get(self.url).text, encoding="UTF-8")
        index = 1
        for t in table:
            t_name = "table" + str(index) + ".xlsx"
            t.to_excel(t_name)
            self.filename.append(t_name)
            index += 1

    def get_filename(self):
        return self.filename
