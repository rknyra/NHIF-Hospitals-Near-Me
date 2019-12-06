from django import forms
from .models import Hospital, Review


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Review
        fields=['reviews']
