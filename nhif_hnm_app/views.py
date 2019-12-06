from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ReviewsForm


#views

#index/landing
def index(request):
    
    return render(request, 'index.html', locals())

#find hospitals
def search(request):
    
    return render(request, 'hnm_pages/find_hospitals.html', locals())

#hospital reviews
def reviews(request, hospital_id):
    reviewsForm = ReviewsForm()
    if request.method == 'POST':
        reviewsForm = ReviewsForm(request.POST)
        if reviewsForm.is_valid():
            form = reviewsForm.save(commit=False)
            form.user=request.user
            form.hospital=get_object_or_404(Hospital,pk=hospital_id)
            form.save()
    
    return redirect('reviews', hospital_id)