from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # now = datetime.datetime.now()
    # html = "<html><body>the time is %s</body></html>" % now
    return render(request,'cpc_web/home.html')
