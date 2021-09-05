from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
# import ast
from pytube import YouTube
import os
import concurrent.futures
import json
# print('Task Completed!') 
PATH = 'D:\drivers\chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
drivers = []
bad = []
nnn = 8
def downY(i):
    yt = YouTube(i)
    video = yt.streams.filter(only_audio=True).first()
    destination = "D:\Music\ " + pathaa
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    # print(yt.title + " has been successfully downloaded.")
def getDrivers(n):
    for  i in range(0,n):
        i = webdriver.Chrome(PATH,options=chrome_options)
        drivers.append(i)
# driver = webdriver.Chrome(PATH,options=chrome_options)
    # print(qwer)
def urlenc(a):
    c = ''
    b = {
        '#':'%23',
        '$':'%24',
        '%':'%25',
        '&':'%26',
        "'"	'%27'
        '+':'%2B',
        ',':'%2C',
        '/':'%2F',
    }
    for i in a:
        if i in b.keys():
            c = c+b[i]
        else:
            c = c + i
    c = c.replace(' ', '+')
    c = c.replace('(', '%28')
    c = c.replace(')', '%29')
    return c
# def getjson(qwer):
#     op = []
#     for i in qwer['tracks']['items']:
#         i['playlist'] = []
#         i['playlist'].append(qwer['name'])
#         i['nummm'] = len(op)
#         op.append(i)
#     print(len(op))
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         for j in executor.map(getYou,op):
#             print(j['track']['name'])
def getYou(a):
    global asdasdasd
    a['trials'] = 0
    while a['trials'] < 3:
        try:
            drivers[a['num']%nnn].get("https://www.youtube.com/results?search_query="+urlenc(str(a['track']['name']) + " " +"by"+" "+ str(a['track']['artists'][0]['name']))+'&sp=EgIQAQ%253D%253D')
            drivers[a['num']%nnn].set_page_load_timeout(5)
            time.sleep(2)
            a['soup'] = BeautifulSoup(drivers[a['num']%nnn].page_source, "html.parser")
            for i in (a['soup'].select('#contents > ytd-video-renderer'))[0:5]:
                try:
                    a['d'] = (i.select('#overlays > ytd-thumbnail-overlay-time-status-renderer > span')[0].text.strip())
                except:
                    continue
                a['mili'] = int(a['d'].split(':')[0])*60000 + int(a['d'].split(':')[1])*1000
                if a['mili']>= int(a['track']['duration_ms'])-10000 and a['mili']<=int(a['track']['duration_ms'])+10000:
                    a['ootube'] = str(i.select('a.yt-simple-endpoint')[0]['href'])
                    break
            # a['download'] = "https://yt1s.com/youtube-to-mp3/en2?q=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D"+a['ootube'].split('=')[1]
            # # while 'youtube' in a['download']:
            # trial2 = 0
            # while 'youtube' in a['download']:
            #     drivers[a['num']%nnn].get(a['download'])
            #     drivers[a['num']%nnn].implicitly_wait(5)
            #     for i in range(2):
            #         try:
            #             time.sleep(1)
            #             a['download'] = drivers[a['num']%nnn].find_element_by_id("asuccess").get_attribute('href')
            #             break
            #         except:
            #             pass
            #     try:
            #         if(drivers[a['num']%nnn].find_element_by_css_selector('#search-result > div.error > p').text != ''):
            #             break
            #         continue
            #         # print(drivers[a['num']%nnn].find_element_by_css_selector('#search-result > div.error > p').text)
            #     except:
            #         pass
            del a['soup']
            json.dump(a, asdasdasd, indent=4)
            asdasdasd.write(',\n')
            downY("https://www.youtube.com/watch/v"+a['ootube'])
            return a
        except:
            a['trials'] = a['trials']+1
            continue
    if a['trials'] >= 3:
        bad.append(a)
        print(a['track']['name'] + '    Failed')
        return "utter failure"
def divide_chunks(l, n):
    for i in range(0, len(l), n): 
        yield l[i:i + n]
def getSpot(a):
    global pathaa
    global asdasdasd
    res = requests.get(a)
    time.sleep(1)
    x = res.text.split('Spotify.Entity = ')[1].split(',"available_markets"')[0]+'}'
    qwer = json.loads(x)
    pathaa = qwer['name'].replace('  ','_').replace('-', '').replace(' ', '').lower()
    asdasdasd = open(str(pathaa+'.json'), 'w')
    op = []
    for i in qwer['tracks']['items']:
        i['playlist'] = []
        i['playlist'].append(qwer['name'])
        i['num'] = len(op)
        op.append(i)
    print(len(op))
    x = list(divide_chunks(op,nnn))
    for asd in x:
        with concurrent.futures.ThreadPoolExecutor(max_workers=nnn) as executor:
            for j in executor.map(getYou,asd):
                try:
                    print(j['track']['name'])
                except:
                    continue
            executor.shutdown(wait=True)

def leftOver(a):
    global bad
    bad = []
    x = list(divide_chunks(a,nnn))
    for asd in x:
        with concurrent.futures.ThreadPoolExecutor(max_workers=nnn) as executor:
            for j in executor.map(getYou,asd):
                try:
                    print(j['track']['name'])
                except:
                    continue
        executor.shutdown(wait=True)
getDrivers(nnn)
playlists = ['https://open.spotify.com/playlist/57bmr0v0mEEyVUlZ7PKYV5?si=UUOzg4ThT7yKMuE2mHQg3w&utm_source=whatsapp','https://open.spotify.com/playlist/5Xs8Ww26cV39DZz035tt0w?si=oNtKucOyShmbgwKM_eSt5g&utm_source=whatsapp', 'https://open.spotify.com/playlist/3uudS2DVdPTcRNT7HHfUIJ?si=XtcK6TKoR1SRNMnccC0_7Q&utm_source=whatsapp', 'https://open.spotify.com/playlist/4PWQV9dQpT7As9OTZBqrR8?si=vI6AdH0bS2Gq5nhuIaORMg&utm_source=whatsapp', 'https://open.spotify.com/playlist/0tLAnPmh7VpPKBu8v6pZXd?si=1TL6_iqJQyqpih81Xcr-yw&utm_source=whatsapp', 'https://open.spotify.com/playlist/1w6t6OLaO3qLHJ176Ub4Yg?si=qHL1mFcbQpSVxHo60QZyeg&utm_source=whatsapp', 'https://open.spotify.com/playlist/38iI10NJQ5HY0ilCItMz5r?si=8_LJ41FhRSClW4mpK7bAZA&utm_source=whatsapp', 'https://open.spotify.com/playlist/3YeZoDpkX968dobH8Ek1Is?si=w1bS21AKQbmdOu4JJCIrEw&utm_source=whatsapp']
for playlist in playlists:
    getSpot(playlist)
    print('BAAAAAAAD SOOOOONGSSSSSSSSSS')
    print(len(bad))
    leftOver(bad)
    print('SUPPPPEEERRRRR BAAAAAAAD SOOOOONGSSSSSSSSSS')
    print(len(bad))
    for i in bad:
        print(i['track']['name'])