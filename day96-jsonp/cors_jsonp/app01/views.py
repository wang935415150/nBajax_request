from django.shortcuts import render,HttpResponse

def get_data(request):
    import time
    time.sleep(2)
    func_name = request.GET.get('callback')
    return HttpResponse('%s("机密数据")' %func_name)
