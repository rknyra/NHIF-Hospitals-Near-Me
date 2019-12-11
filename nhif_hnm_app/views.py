from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ReviewsForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from .serializers import HospitalSerializer
from .permissions import isAdminOrReadOnly


#views

#index/landing
def index(request):
    
    return render(request, 'index.html', locals())


#search page
def searchPage(request):
    
    return render(request, 'hnm_pages/find_hospitals.html', locals())


#search feature
def searchHospital(request):
    reviewsForm = ReviewsForm()

    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_hospitals = Hospital.objects.filter(location__icontains=search_term)
        message = f"{search_term}"
        
        return render(request, 'hnm_pages/search_results.html', locals())
    else:
        message = "You haven't searched for any hospital"
        return render (request, 'hnm_pages/search_results.html', locals())


#all hospitals reviews
def reviews(request):
    hospitals = Hospital.objects.all()
    reviewsForm = ReviewsForm()

    return render (request, 'hnm_pages/hospital_reviews.html', locals())


#single hospital reviews
@login_required(login_url='/accounts/login')
def singleHospitlaReviews(request, hospital_id):
    reviewsForm = ReviewsForm()
    hospital = get_object_or_404(Hospital,pk=hospital_id)

        
    if request.method == 'POST':
        reviewsForm = ReviewsForm(request.POST)
        if reviewsForm.is_valid():
            form = reviewsForm.save(commit=False)
            form.user=request.user
            form.hospital=get_object_or_404(Hospital,pk=hospital_id)
            form.save()
    return redirect('all_reviews')


class HospitalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows viewing of NHIF-registered hospitals
    """
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [isAdminOrReadOnly]