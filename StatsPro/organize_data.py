class OrganizeData:
    def __init__(self, html_page, url):
        self.page = html_page
        self.data_dict = {}
        self.url = url
        self.no_tables = False
        self.visited = False

    def organize(self):
        tables = self.page.cssselect('table')
        if len(tables) != 0:
            print()
            # for tb in tables:
            #     table = ''
            #     for th in tb.cssselect('th'):
            #         table += th.text_content().strip() + "*"
            #     trs = tb.cssselect('tr')
            #     for tr in trs:
            #         tds = tr.cssselect('td')
            #         for td in tds:
            #             cell_text = td.text_content().strip()
            #             table += cell_text
            #             table += '*'
            #         table += ' \n'
            #     table += '\n'
            #     if self.url not in self.data_dict.keys():
            #         self.data_dict[self.url] = table
            #     else:
            #         self.visited = True
        else:
            self.no_tables = True

    def return_data(self):
        return self.data_dict

    def return_no_tables(self):
        return self.no_tables
