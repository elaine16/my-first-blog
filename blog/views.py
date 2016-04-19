from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
#criamos um método (def) chamado post_list que aceita o pedido e retornar um método render será processado (para montar) nosso modelo blog/post_list.html