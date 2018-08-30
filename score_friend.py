import requests
s = requests.Session()
import warnings
warnings.filterwarnings('ignore')



songid = "grievouslady"
url = r"https://arcapi.lowiro.com/4/score/song/friend?song_id=%s&difficulty=1&start=0&limit=10"%songid

def loadsongs():
    f = open("song.json","r")
    t = f.read()
    f.close()
    return eval(t)

def getdata():
    res = {}
    header = {
        "Accept-Encoding":"identity",
        "Content-Type":r"application/x-www-form-urlencoded; charset=utf-8",
        "Authorization":"Bearer Clg3N0Og8ngL6+KK4a10IT0rmma9Ft89cZxYDTzb6zQ=",
        "AppVersion":"1.7.2c",
        "User-Agent":r"Dalvik/1.6.0 (Linux; U; Android 4.4.4; G750-T20 Build/KTU84P)",
        "Host":"arcapi.lowiro.com",
        "Connection":"Keep-Alive"
        }
    songlist = loadsongs()
    cons = ["name","song_id","difficulty","score","shiny_perfect_count","perfect_count","near_count","miss_count","rating"]
    for song in songlist:
        for i in range(3):
            url = r"https://arcapi.lowiro.com/4/score/song/friend?song_id=%s&difficulty=%d&start=0&limit=10"%(song["songid"],i)
            print((song["songid"],i))
            resp = s.get(url,headers=header,verify=False)
            resp = eval(resp.text.replace("true","True").replace("false","False"))
            for userdata in resp["value"]:
                line = []
                for c in cons:
                    line.append(userdata[c])
                try:
                    res[userdata["name"]].append(line)
                except:
                    res[userdata["name"]]=[line]
    for user in list(res):
        res[user] = sorted(res[user],key=lambda u:u[8],reverse=True)
    return res

def addfriend(uid):
    url = r"https://arcapi.lowiro.com/4/friend/me/add"
    header = {
        "Accept-Encoding":"identity",
        "User-Agent":r"Dalvik/1.6.0 (Linux; U; Android 4.4.4; G750-T20 Build/KTU84P)",
        "Content-Length":str(len(uid)+12),
        "Content-Type":r"application/x-www-form-urlencoded; charset=utf-8",
        "AppVersion":"1.7.2c",
        "Authorization":"Bearer Clg3N0Og8ngL6+KK4a10IT0rmma9Ft89cZxYDTzb6zQ=",
        "Host":"arcapi.lowiro.com",
        "Connection":"Keep-Alive"
        }
    body = "friend_code="+uid
    resp = s.post(url,headers=header,data=body.encode(),verify=False)
    print(resp.text)
def deletefriend(fid):
    url = r"https://arcapi.lowiro.com/4/friend/me/delete"
    header = {
        "Accept-Encoding":"identity",
        "User-Agent":r"Dalvik/1.6.0 (Linux; U; Android 4.4.4; G750-T20 Build/KTU84P)",
        "Content-Length":str(len(fid)+10),
        "Content-Type":r"application/x-www-form-urlencoded; charset=utf-8",
        "AppVersion":"1.7.2c",
        "Authorization":"Bearer Clg3N0Og8ngL6+KK4a10IT0rmma9Ft89cZxYDTzb6zQ=",
        "Host":"arcapi.lowiro.com",
        "Connection":"Keep-Alive"
        }
    body = "friend_id="+fid
    resp = s.post(url,headers=header,data=body.encode(),verify=False)
    print(resp.text)
def getfriendlist():
    url = r"https://arcapi.lowiro.com/4/compose/aggregate?calls=%5B%7B%20%22endpoint%22%3A%20%22user%2Fme%22%2C%20%22id%22%3A%200%20%7D%2C%20%7B%20%22endpoint%22%3A%20%22purchase%2Fbundle%2Fpack%22%2C%20%22id%22%3A%201%20%7D%5D"
    header = {
        "Accept-Encoding":"identity",
        "Content-Type":r"application/x-www-form-urlencoded; charset=utf-8",
        "Authorization":"Bearer Clg3N0Og8ngL6+KK4a10IT0rmma9Ft89cZxYDTzb6zQ=",
        "AppVersion":"1.7.2c",
        "User-Agent":r"Dalvik/1.6.0 (Linux; U; Android 4.4.4; G750-T20 Build/KTU84P)",
        "Host":"arcapi.lowiro.com",
        "Connection":"Keep-Alive"
        }
    resp = s.get(url,headers=header,verify=False)
    resp = eval(resp.text.replace("true","True").replace("false","False"))
    return resp["value"][0]["value"]["friends"]
fl = getfriendlist()

