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
    task_id = "span_task_" + str(task.id)
    task.task_done_flag = status
    task.save()
    data = {
    'data_saved' : 1,
    'span_id' : task_id,
    }
    return JsonResponse(data)

def get_details(request):
    id = request.GET.get('id', False)
    if Task.objects.filter(id = id):
        task = Task.objects.filter(id = id)[0]
    else:
        return HttpResponse("No Task Found")
    detailed_data = {
    'task_title' : task.task_title,
    'task_description' : task.task_description,
    'task_published' : task.task_published,
    'task_scheduled' : task.task_scheduled,
    'task_done_flag' : task.task_done_flag,
    'data_deliverd' : 1,
    }
    return JsonResponse(detailed_data)


def django_to_html_json(request):
    response_data = {}
    response_data['result'] = 'error'
    response_data['message'] = 'Some error message'
    data_json = json.dumps(response_data)
    return JsonResponse(response_data)
