import wikipediaapi
import requests

WIKIPEDIA = wikipediaapi.Wikipedia('en')
DATA = requests.get('https://raw.githubusercontent.com/mledoze/countries/master/countries.json').json()