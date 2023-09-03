from django import forms
from .models import ReviewRating, Comment


class ReviewRatingForms(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']
        

class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_name', 'comment_body']    