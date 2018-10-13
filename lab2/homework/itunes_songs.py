from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url =  'https://www.apple.com/itunes/charts/songs'

conn = urlopen(url)

raw_data = conn.read()

webpage_text = raw_data.decode("utf-8")
# print(webpage_text)
# f = open('apple.html', 'wb')
# f.write(raw_data)
# f.close()

soup = BeautifulSoup(webpage_text, "html.parser")
sec = soup.find("section", "section chart-grid")

# print(sec)



li_list = sec.find_all('li')
# print(li_list)
news_list = []

for li in li_list:
    a = li.h3.a
    song = a.string
    b = li.h4.a
    artist = b.string

    print(song)
    print(artist)
    news = {
        "Song": song,
        "Artist" : artist,
    }

    news_list.append(news)
print(*news_list, '\n', sep= ' ******** ')
print(soup.prettify())
# pyexcel.save_as(records = news_list, dest_file_name = 'itunes.xlsx')