from lxml import html
import requests
from datetime import datetime, timedelta


class HolidayChecker:
    def __init__(self, url):
        self.url = url
        self.html = self.scrape_data()
        self.dates = None
        self.data_table = self.get_holidays(self.html)

    def get_holiday_desc(self, date):
        try:
            return self.data_table[date]
        except KeyError:
            return 'Date is not a Holiday!'

    def get_data_table(self):
        return self.data_table

    def scrape_data(self):
        response = requests.get(self.url)
        source = response.content
        html_elem = html.document_fromstring(source)
        return html_elem

    def get_holidays(self, html_elem):
        data_table = {}
        tables = html_elem.cssselect('table')
        table1 = tables[0]
        year = self.url[self.url.rfind('-')+1:self.url.rfind('/')]
        trs = table1.cssselect('tr')
        for tr in trs:
            output_row = []
            tds = tr.cssselect('td')
            for td in tds:
                cell_text = td.text_content().strip()
                cell_text = cell_text.replace(u'\xa0', u' ')
                if 'Sept' in cell_text:
                    cell_text.replace('Sept', 'Sep')
                output_row.append(cell_text)
            if "(NO CLASSES" in output_row[1]:
                date = output_row[0]
                if '-' in output_row[0]:
                    dates = []
                    temp = date[date.index(' '):]
                    days = temp.split('-')
                    # takes two dates split by '-' and provides a full range of dates
                    for day in days:
                        month = date[0:date.index(' ')]
                        d = month + ' ' + day + ' ' + year
                        if '.' in d:
                            dates.append(datetime.strptime(d, '%b. %d %Y'))
                        else:
                            dates.append(datetime.strptime(d, '%B %d %Y'))
                    full_range = []
                    delta = dates[1] - dates[0]
                    for i in range(delta.days + 1):
                        full_range.append(dates[0] + timedelta(days=i))
                    for date in full_range:
                        data_table[date] = output_row[1]
                elif '.' in output_row[0]:
                    date2 = date
                    if 'Sept.' in date:
                        date2 = date[0:3] + date[4:]
                    new_date = datetime.strptime(date2 + ' ' + year, '%b. %d %Y')
                    data_table[new_date] = output_row[1]
                else:
                    date = datetime.strptime(date + ' ' + year, '%B %d %Y')
                    data_table[date] = output_row[1]
        return data_table

    # noinspection PyMethodMayBeStatic
    def is_holiday(self, date):
        return date in self.data_table.keys()
