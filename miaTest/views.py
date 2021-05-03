from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
import json
import simplejson
from django.http import JsonResponse
from miaTest.models import *
# 将请求定位到index.html文件中
def index(request):
    return render(request, 'index.html')
# Create your views here.
def log_on(request):
    return render(request, 'log_on.html')
#注册
def register(request):
    return render(request, 'register.html')

#用户注册处理
def register_handle(request):
    """进行注册处理"""
    req = simplejson.loads(request.body)
    user_id = req[0]['user_id']
    user_phone = req[0]['user_phone']
    user_password = req[0]['user_password']
    num = user.objects.filter(user_id=user_id).count()
    if num > 0:
        print("该账号已被注册")
    else:
        mzl = user()
        mzl.user_id = user_id
        mzl.user_password = user_password
        mzl.user_phone = user_phone
        mzl.save()
    return JsonResponse({'flag': num})

#界面跳转函数 有点问题
def jumpurl(request):
    req = simplejson.loads(request.body)
    jurl = req[0]['jurl']
    print(jurl)
    return redirect(jurl)

#管理员注册处理
def ad_register_handle(request):
    req = simplejson.loads(request.body)
    ad_ac = req[0]['ad_active']
    ad_id = req[0]['ad_id']
    ad_password = req[0]['ad_password']
    num = ad_active.objects.filter(ad_ac=ad_ac).count()
    num1 = admin.objects.filter(ad_id=ad_id).count()
    print(num, num1)
    if num == 1:
        if num1 == 0:
            mg = ad_active()
            mg.ad_id = ad_id
            mg.ad_password = ad_password
            mg.save()
    return JsonResponse({'flag': num,
                         'flag1': num1})

def customer_log_on(request):
    req = simplejson.loads(request.body)
    user_id = req[0]['user_id']
    user_password = req[0]['user_password']
    num = user.objects.filter(user_id=user_id, user_password=user_password).count()
    print(num)
    return JsonResponse({'flag': num })

def ad_log_on(request):
    req = simplejson.loads(request.body)
    ad_id = req[0]['ad_id']
    ad_password = req[0]['ad_password']
    num = admin.objects.filter(ad_id=ad_id, ad_password=ad_password).count()
    return JsonResponse({'flag': num})