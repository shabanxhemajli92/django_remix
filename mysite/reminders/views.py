from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
import json
from .models import Reminder

def index(request):
    reminders=Reminder.objects.all()
    empty_lst=[]
    for reminder in reminders:
        print(reminder)
        empty_lst.append({'id':reminder.id,'title':reminder.title,'description':reminder.description})
    print(empty_lst)
    my_dict={'reminders':empty_lst}
    return JsonResponse(my_dict)

# @csrf_exempt -> my code
# def new_reminder(request):
#     data = json.loads(request.body)
#     reminder=Reminder.objects.create(title=data['title'],description=data['description'])
#     my_dict={'title':reminder.title,'description':reminder.description,'id':reminder.id}
#     return JsonResponse(my_dict)
#     #return HttpResponse("hELLO WORLD")    

@csrf_exempt
def new_reminder(request):
    try:
        data = json.loads(request.body)
        title = data.get("title")
        description = data.get("description")
        reminder = Reminder.objects.create(title=title, description=description)
        return JsonResponse(reminder.to_json())
    except:
        return JsonResponse({"message": "Something bad happened"}, status=500)