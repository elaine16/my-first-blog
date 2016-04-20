from django.shortcuts import render
from django.utils import timezone
from .models import Post # inclui o modelo que temos escrito em models.py
#O ponto depois de from significa o diretório atual ou o aplicativo atual. Como views.py e models.py estão no mesmo diretório podemos simplesmente usar . e o nome do arquivo (sem .py). Então nós importamos o nome do modelo (Post).

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    #return render(request, 'blog/post_list.html', {})
    #criamos um método (def) chamado post_list que aceita o pedido e retornar um método render será processado (para montar) nosso modelo blog/post_list.html

    return render(request, 'blog/post_list.html', {'posts': posts})
    #'blog/post_list.html' : e um arquivo de template
    #{} é um lugar em que podemos acrescentar algumas coisas para que o template use.