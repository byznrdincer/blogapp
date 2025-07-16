from django import forms 
from .models import Post,Comments

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content']
        
class CommentsForm(forms.ModelForm):
    class Meta:
         model=Comments
         fields=['name','email','body']
