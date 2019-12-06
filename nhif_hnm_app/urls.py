from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('search/',views.searchPage,name='search'),
    path('all-reviews/',views.reviews,name='all_reviews'),
    path('single-hospital-reviews/<int:hospital_id>',views.singleHospitlaReviews,name='single_hospital_reviews'),
    path('search-hospitals/', views.searchHospital,name='search_hospitals')
]
