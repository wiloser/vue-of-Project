from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def hello(request):
    data = {'context': 'fuck you', }
    return JsonResponse(data, safe=False)


@csrf_exempt
def login(request, param=None):
    if param is None:
        param = {}
    print(str(request))
    print(param)
    data = {'message': 'yes', 'code': 200}
    return JsonResponse(data, safe=False)
