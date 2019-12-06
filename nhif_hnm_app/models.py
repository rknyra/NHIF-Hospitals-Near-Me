from django.db import models
from django.contrib.auth.models import User
import datetime as dt

#hospital model
class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    website = models.URLField(max_length=350, null=True, blank=True)
    
    def save_hospital(self):
            self.save()
        
    @classmethod
    def get_hospital(cls,location):
        hospitals = cls.objects.filter(location=location)
        
        return hospitals
        
    def __str__(self):
        return str(self.hospital_name)


class Review(models.Model):
    reviews = models.CharField(max_length=1000, blank=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def save_review(self):
        self.save()
        
    @classmethod
    def get_reviews(cls,id):
        reviews = cls.objects.filter(hospital__id=id)
        
        return reviews
        
    def __str__(self):
        return str(self.reviews)