from progress.bar import IncrementalBar
from data import WIKIPEDIA

class Countries_iterator():
    def __init__(self, data:list):
        self.data = data
        self.index = 0
        self.result = []
        self.bar = IncrementalBar('Загрузка ссылок из "Википедии"', max = len(self.data))
    def __iter__(self):
        return self
    def __next__(self):
        try:
            index_now = self.index
            country_name = self.data[index_now]["name"]["common"]
            # print(country_name)
            # print(wikipedia.page(country_name))
            country_page = WIKIPEDIA.page(country_name).fullurl
            self.result.append({country_name : country_page})
            self.index += 1
            self.bar.next()
            return f'{country_name} - {country_page}\n'
        except IndexError:
            self.bar.finish()
            raise StopIteration()