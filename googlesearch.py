__author__ = 'saandeepa'
from google import search
for url in search('India', stop=20):
    print(url)