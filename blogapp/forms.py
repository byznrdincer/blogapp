from django import forms 
from .models import Post,Comments, UserProfile

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content']
        
class CommentsForm(forms.ModelForm):
    class Meta:
         model=Comments
         fields=['name','email','body']
class ProfileUpdateForm(forms.ModelForm):  # <-- Yeni eklenen form
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio']