from django.contrib import admin
from .models import Hospital, Review
from django.contrib.auth.models import User

#regisering models
admin.site.register(Hospital)
admin.site.register(Review)