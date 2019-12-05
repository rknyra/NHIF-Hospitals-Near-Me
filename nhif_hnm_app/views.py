from django.shortcuts import render



#views

#index/landing
def index(request):
    
    return render(request, 'index.html', locals())
