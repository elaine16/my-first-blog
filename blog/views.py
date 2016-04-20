from django.shortcuts import redirect # importação para ir à página de post_detail para o recém-criado blog post
from django.utils import timezone
from .models import Post # inclui o modelo que temos escrito em models.py
from django.shortcuts import render, get_object_or_404
from .forms import PostForm


#O ponto depois de from significa o diretório atual ou o aplicativo atual. Como views.py e models.py estão no mesmo diretório podemos simplesmente usar . e o nome do arquivo (sem .py). Então nós importamos o nome do modelo (Post).

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    #return render(request, 'blog/post_list.html', {})
    #criamos um método (def) chamado post_list que aceita o pedido e retornar um método render será processado (para montar) nosso modelo blog/post_list.html

    return render(request, 'blog/post_list.html', {'posts': posts})
    #'blog/post_list.html' : e um arquivo de template
    #{} é um lugar em que podemos acrescentar algumas coisas para que o template use.

def post_detail (request, pk): # view para o link url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
