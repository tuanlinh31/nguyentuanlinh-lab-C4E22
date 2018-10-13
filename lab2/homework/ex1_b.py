from youtube_dl import YoutubeDL
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
    options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
    }
    dl = YoutubeDL(options)
    dl.download(['con điên TAMKA PKL'])

# print(*news_list, '\n', sep= ' ******** ')
# print(soup.prettify())
    options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download(['Nhớ mưa sài gòn lam trường'])

news_list.append(news)
# pyexcel.save_as(records = news_list, dest_file_name = 'itunes.xlsx')
