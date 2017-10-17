from django.shortcuts import render
import requests

# def index(request):
#     response = requests.get('http://127.0.0.1:8000/get_data.html')
#     return render(request,'index.html',{'response':response})
#

def index(request):

    return render(request,'index.html')
