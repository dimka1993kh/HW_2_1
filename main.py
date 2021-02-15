from iterator import Countries_iterator
from data import DATA

if __name__ == '__main__':
    first_search = Countries_iterator(DATA)
    with open('Countries_links.txt', 'w', encoding='utf-8') as document:
        for country in first_search:
            document.write(''.join(country))
    