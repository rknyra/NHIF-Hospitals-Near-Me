from django import forms
from .models import Hospital, Review


class ReviewsForm(forms.Form):
    class Meta:
        model = Review
        fields=['reviews']
