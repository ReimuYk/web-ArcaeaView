# coding:UTF-8
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, Template 
import base64
import json
import os

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
