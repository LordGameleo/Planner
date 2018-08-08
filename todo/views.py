from django.http import HttpResponse
from django.shortcuts import render
from todo.models import *
from django.http import JsonResponse
def dashboard(request):
    scheduled_tasks = Task.objects.all()
    return render(request, 'home/dashboard.html', {'scheduled_tasks' : scheduled_tasks})

def change_task_status(request):
    id = request.GET.get('id', False)
    status = request.GET.get('status', False)
    report = str(id) + " " + str(status)

    if Task.objects.filter(id = id):
        task = Task.objects.filter(id = id)[0]
    else:
        return HttpResponse("No Task Found")
    if status == 'true':
        status = True
    else:
        status = False

    task.task_done_flag = status
    task.save()
    data = {
    'data_saved' : 1 
    }
    return JsonResponse(data)

def django_to_html_json(request):
    response_data = {}
    response_data['result'] = 'error'
    response_data['message'] = 'Some error message'
    data_json = json.dumps(response_data)
    return JsonResponse(response_data)
