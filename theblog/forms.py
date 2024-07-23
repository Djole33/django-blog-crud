from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for category in choices:
    choice_list.append(category)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippets', 'header_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), # daje bootstrap styling formi za pravljenje postova
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 
                                             'value': '', 
                                             'id': 'elder', # id kolona je potrebna javascriptu da bi identifikovao koji user je loginovan
                                             'type': 'hidden'}), 
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippets': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'snippets')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}), #daje bootstrap styling formi za pravljenje postova
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippets': forms.Textarea(attrs={'class': 'form-control'}),
        }
        