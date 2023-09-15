from django.http import HttpResponse, JsonResponse


def hello(request):
    data = {'context': 'fuck you', }
    return JsonResponse(data, safe=False)


def login(request):
    data = {''}
    return JsonResponse(data, safe=False)
