from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    numbers=range(0, 2000)
    context={"numbers": numbers}
    return render(request,"home/index.html",context)

def hello_tojson(request):
    return JsonResponse({'name':'Shaban the best'}) 