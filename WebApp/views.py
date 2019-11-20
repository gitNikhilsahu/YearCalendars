from django.shortcuts import render
from datetime import datetime
import calendar
from calendar import HTMLCalendar

def MyCalView(request):
    y = 2019
    m = 6
    nik = "- %s %s" % ('NOV', y)
    cal = HTMLCalendar().formatyear(y, m)
    dic = {'nik': nik, 'cal': cal}
    return render(request, 'WebApp/Cal.html', context=dic)
    