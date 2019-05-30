 from django import forms
 from .models import post, Category, Tag

class addPost(forms.ModelForm):
    class Meta:
        model = post
        fields = {'title','date','content', 'category','tags', 'author'}
