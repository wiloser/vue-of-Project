from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# 定义一个简单的装饰器函数
def decorator(func):
    def wrapper():
        print('start Get')
        func()
        print('end Get')

    return wrapper


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
