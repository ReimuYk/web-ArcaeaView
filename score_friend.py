import requests
s = requests.Session()
import warnings
warnings.filterwarnings('ignore')

header = {
    "Accept-Encoding":"identity",
    "Content-Type":r"application/x-www-form-urlencoded; charset=utf-8",
    "Authorization":"Bearer Clg3N0Og8ngL6+KK4a10IT0rmma9Ft89cZxYDTzb6zQ=",
    "AppVersion":"1.7.2c",
    "User-Agent":r"Dalvik/1.6.0 (Linux; U; Android 4.4.4; G750-T20 Build/KTU84P)",
    "Host":"arcapi.lowiro.com",
    "Connection":"Keep-Alive"
    }

songid = "grievouslady"
url = r"https://arcapi.lowiro.com/4/score/song/friend?song_id=%s&difficulty=1&start=0&limit=10"%songid

def loadsongs():
    f = open("song.json","r")
    t = f.read()
    f.close()
    return eval(t)


##resp = s.get(url,headers=header,verify=False)
##print(resp.text)
songlist = loadsongs()
cons = ["name","song_id","difficulty","score","shiny_perfect_count","perfect_count","near_count","miss_count","rating"]
out = open("output.csv","w")
for song in songlist:
    for i in range(3):
        url = r"https://arcapi.lowiro.com/4/score/song/friend?song_id=%s&difficulty=%d&start=0&limit=10"%(song["songid"],i)
        print((song["songid"],i))
        resp = s.get(url,headers=header,verify=False)
        resp = eval(resp.text.replace("true","True").replace("false","False"))
        for userdata in resp["value"]:
            for c in cons:
                out.write(str(userdata[c]))
                out.write(',')
            out.write('\n')
out.close()

