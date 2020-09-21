from django import forms
from .models import *

# but this is not great as ir is not dynamic
# choice = [('coding','coding'),('entertainment','entertainment'),('sports','sports')]

choice = Category.objects.all().values_list('name','name')
ch_lst = []
for i in choice:
    ch_lst.append(i)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','category','body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'name','id':'uservalue'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category':forms.Select(choices=ch_lst, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})

        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})

        }