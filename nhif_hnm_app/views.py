from django.shortcuts import render



#views

#index/landing
def index(request):
    
    return render(request, 'index.html', locals())

#find hospitals
def search(request):
    
    return render(request, 'hnm_pages/find_hospitals.html', locals())

#hospital reviews
def reviews(request):
    
    return render(request, 'hnm_pages/hospital_reviews.html', locals())