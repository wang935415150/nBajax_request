from django.shortcuts import render,HttpResponse

# def get_data(request):
#     import time
#     time.sleep(2)
#     func_name = request.GET.get('callback')
#     return HttpResponse('%s("机密数据")' %func_name)


def get_data(request):
    if request.method == "OPTIONS":
        # 预检
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = "*"
        # response['Access-Control-Allow-Methods'] = "PUT"
        response['Access-Control-Allow-Headers'] = "xxx"
        return response

    elif request.method == "GET":
        response = HttpResponse("机密数据")
        response['Access-Control-Allow-Origin'] = "*"

        return response
