from django import forms
from .models import Post

class PostForm(forms.ModelForm): #PostForm é o nome do formulário  forms.ModelForm cria o formulário pelo Django

    class Meta:
        model = Post
        fields = ('title', 'text',)
# agora devemos criar: um link para a página, uma URL, uma view e um template.