from django.http import HttpResponse, JsonResponse


def hello(request):
    data = {'context': 'fuck you', }
    return JsonResponse(data)
