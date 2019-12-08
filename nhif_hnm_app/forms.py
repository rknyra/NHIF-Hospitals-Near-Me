from django import forms
from .models import Hospital, Review


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Review
        fields=['reviews']
        widgets = {
            'reviews': forms.TextInput(attrs={'placeholder': 'Share your review/experience at this hospital...'})
        }