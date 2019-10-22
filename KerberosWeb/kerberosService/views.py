from django.http import JsonResponse
import json
from .api_urls import apipatterns
import urllib
from urllib import parse


def API(request):
    result = {'type':'error','data':{}}
    if request.method == 'POST':
        print(request.POST)
        type = request.POST['type']
        data = json.loads(request.POST['data'])
        if type and data:
            ##注释的是通过循环来匹配请求类型进行处理
            # for key,fun in apipatterns:
            #     result['type'] = 'success'
            #     result['data'] = fun(data)
            #     break
            ##下面是通过字典取值处理请求类型
            dicts = dict(apipatterns)
            if type in dicts.keys():
                result['type'] = 'success'
                result['data'] = dicts[type](data)
            else:
                result['data'] = 'no type %s'%type
        else:
            result['data'] = 'type or data not be null'
    elif request.method == 'GET':
        result['data'] = 'The request must be post'
    return JsonResponse(result)