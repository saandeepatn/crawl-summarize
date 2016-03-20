__author__ = 'saandeepa'
__author__ = 'saandeepa'
import naivetsshlomi
from google import search
import urllib
from bs4 import BeautifulSoup
def get_sites(search_text):
    print "Dowloading urls.."
    urllist=[]
    for url in search(search_text, stop=20):
        urllist.append(url)
    return urllist

def textextract(search_text,url):



    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on eachU
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    #print(text)
    naivetsshlomi.mainshlomi(search_text,text)

search_text=raw_input("Enter the subject of summary:")
urllist=[]
urllist=get_sites(search_text)

for url in range(2):
    print(urllist[url])
    print("Extracting from "+urllist[url])
    textextract(search_text,urllist[url])
