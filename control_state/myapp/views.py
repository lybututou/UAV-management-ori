import win32con
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import *
import os,datetime
import win32api
# Create your views here.
def login(request):
    return render(request,'myapp/login_window.html')

def regist(request):
    return render(request, 'myapp/regist.html')

def regist_sql(request):
    ob = Users()
    ob.username = request.POST.get('Username')
    # print(ob.username)
    try:
        user = Users.objects.get(username = ob.username)
        return HttpResponse('''<script> alert("用户已被注册");location.href="regist";</script>''')
    except:
        ob.password = request.POST.get('Password')
        rightnum = request.POST.get('Rightnumber')
        if (rightnum == '0001'):
            ob.right = '任务操作人员'
        else:
            ob.right = '普通工作人员'
        ob.save()
        return HttpResponse('''<script> alert("注册成功！~");location.href = "/";</script>''')
    # if ( user == []):
    #     ob.password = request.POST.get('Password')
    #     ob.save()
    #     return HttpResponse('''<script> alert("注册成功！~");location.href = "{%url 'login'%}";</script>''')
    # else :
    #     return HttpResponse('''<script> alert("用户已被注册");location.href = "{% url 'regist' %}";</script>''')

def flash(request):
    ulist = Station.objects.all()
    context = {'stationlist': ulist}
    return render(request, 'myapp/Station_Select.html', context)

def Login_judgement(request):
    user = Users.objects.get(username= request.POST.get('Username'))
    if request.POST['Password'] == user.password:
        ulist = Station.objects.all()
        rightnum = 0
        if user.right == '任务操作人员':
            rightnum = 1
        if user.right == '普通工作人员':
            rightnum = 2
        context = {'stationlist':ulist,'rightnum':rightnum}
        print(context)
        return render(request,'myapp/Station_Select.html',context)
    else:
        return HttpResponse('<script> alert("账号或密码错误");location.href = "/";</script>')

def muchao(request,station_id = 0,rightnum = 0):
    muchao_info = info_muchao.objects.filter(station_id=station_id).last()
    context = {'last_data': muchao_info, 'station_id': station_id,'rightnum':rightnum}
    return render(request,'myapp/母巢.html',context)

def station(request,station_id = 0,rightnum = 0):
    # print(station_name)
    station_info = info_data.objects.filter(station_id=station_id).last()
    print(station_info)
    context = {'last_data':station_info,'station_id':station_id,'rightnum':rightnum}
    print(context)
    print(rightnum)
    if rightnum == 1:
        return render(request, 'myapp/work_UAV.html', context)
    if rightnum == 2:
        return render(request, 'myapp/station_look.html',context)

def mission_go(request,station_id = 0,rightnum=0):
    ob = mission()
    ob.station_id = station_id
    ob.Chang = request.POST.get('Chang')
    ob.Wei = request.POST.get('Wei')
    ob.Path = request.POST.get('path')
    ob.save()
    win32api.MessageBox(0,'任务发布成功','中广核',win32con.MB_OK)
    station_info = info_data.objects.filter(station_id=station_id).last()
    # print(station_info)
    context = {'last_data': station_info,'station_id':station_id,'rightnum':rightnum}
    if rightnum == 1:
        return render(request, 'myapp/work_UAV.html', context)
    if rightnum == 2:
        return render(request, 'myapp/station_look.html', context)


def picture(request,station_id = 0):
    ulist = Station.objects.get(station_id=station_id)
    # print(type(ulist))
    date = int(request.POST.get('Pic_date'))
    year = int(date/10000)
    month = int(date/100%100)
    if(month<10):
        month1 = '0'+str(month)
    else:
        month1 = str(month)
    
    day = int(date%100)
    if(day<10):
        day1 = '0'+str(day)
    else:
        day1 = str(day)
    
    givedate = str(year)+"-"+month1+"-"+day1
    path = 'E:\\control_state\\static'+"\\"+str(ulist.name)+"\\"+givedate
    file_name_list = os.listdir(path)
    file_name = []
    # file_name = file_name.replace("[", "").replace("]", "").replace("'", "").replace(",", "\n").replace(" ", "")
    length = len(file_name_list)
    Chang = request.POST.get('Pic_Chang')
    Wei = request.POST.get('Pic_Wei')
    date_from = request.POST.get('Pic_date')
    print(date_from)
    context = {'station_name':ulist,'length':length,'chang':Chang,'wei':Wei,'date_from':date_from}
    print(context)
    return render(request, 'myapp/picture.html',context)

def add(request):
    return render(request, 'myapp/add.html')

def add_to_sql(request):
    ob = Station()
    ob.name = request.POST.get('stationName')
    ob.station_id = request.POST.get('stationID')
    try:
        user = Station.objects.get(name=ob.name)
        return HttpResponse('''<script> alert("此站台已经存在！");location.href="add_station";</script>''')
    except:
        ob.save()
        return HttpResponse('''<script> alert("站台添加成功");location.href="flash";</script>''')

def delete(request):
    return render(request, 'myapp/delete.html')

def delete_to_sql(request):
    ob = Station()
    ob.name = request.POST.get('stationName')
    ob.station_id = request.POST.get('stationID')
    try:
        user = Station.objects.get(name=ob.name)
        user.delete()
        return HttpResponse('''<script> alert("站台删除成功");location.href="flash";</script>''')
    except:
        return HttpResponse('''<script> alert("此站台不存在！");location.href="delete_station";</script>''')
