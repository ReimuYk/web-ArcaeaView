# coding:UTF-8
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, Template 
import base64
import json
import os
import time
import arcview.score_friend as sf

def hello(request):
    resp = [{'errorcode': '100', 'detail': 'Get success'}]
    li = ['l1','l2','l333']
    print("hello")
    return HttpResponse(json.dumps(li), content_type="application/json")

def testlist(req):
    try:
        print(req.GET.get("username"))
    except:
        print("no username")
    data = [{'id':1,'name':'name1'},{'id':2,'name':'name2'}]
    return render(req,'testlist.html',{'testlist':data})

def arclist(req):
    username=req.GET.get("username")
    if username==None:
        return None
    f = open("arcview/userdata/%s.csv"%username,'r')
    data = f.readlines()
    filemt = time.localtime(os.stat("arcview/userdata/%s.csv"%username).st_mtime)
    fmt = time.strftime("%Y-%m-%d %H:%M:%S",filemt)
    f.close()
    for i in range(len(data)):
        tmplist = data[i].split(',')
        tmpdict = {}
        tmpdict["num"] = i+1
        cons=["title","difficulty","score","perfect","pure","far","lost","rating"]
        for j in range(len(cons)):
            tmpdict[cons[j]]=tmplist[j]
        data[i] = tmpdict
    return render(req,'arclist.html',{'songlist':data,'updatetime':fmt})

def refreshdata(req):
    pwd=req.GET.get("password")
    if pwd!="yukidaisuki":
        return HttpResponse("password error")
    dt = sf.getdata()
    for user in list(dt):
        f = open('arcview/userdata/%s.csv'%user,'w')
        for song in dt[user]:
            tmp = []
            for it in song:
                tmp.append(str(it))
            f.write(','.join(tmp))
            f.write('\n')
        f.close()
    return HttpResponse("Success!")
