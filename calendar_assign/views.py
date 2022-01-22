from tkinter import Variable
from django.shortcuts import render, HttpResponse
import calendar



def index(request):
    
    return render(request, 'index.html')


def result(request):
    mon = int(request.GET['mon'])
    hol = str(request.GET['hol'])
    hol = list(map(int, hol.split(",")))
    res=''
    calendar.setfirstweekday(calendar.MONDAY)
    year = 2022
    # months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
    #       'August', 'September', 'October', 'November', 'December']
    month=mon
    for day in range(1, 32):
        try:
            weekday = calendar.weekday(year, month, day)
        except ValueError:
            continue
        if weekday < calendar.SATURDAY and day not in hol:
            t=day
            res+=str(t)
            res+=','
    return render(request, "result.html", {'result': res})