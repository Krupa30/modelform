from django.http import HttpResponse
def index(request):
         return HttpResponse("Hello! Happy to Create First Application.")
def template_demo(request):
    dict_var={'random_var': "I am in views"}
    return render(request,'index.html', context= dict_var)
