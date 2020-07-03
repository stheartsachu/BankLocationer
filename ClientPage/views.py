from django.shortcuts import render,HttpResponse

# Create your views here.
import requests
url = requests.get("https://ancient-taiga-77329.herokuapp.com/api/branch_data")
data = url.json()
def home(request):
    global context
    context = {}
    if request.method == 'POST':
        print(request.POST)
        for i in data:
            if request.POST['ifscinput'] == "%s"% i['ifsc']:
                context=i
                return HttpResponse(context)
    return render(request,"index.html")

