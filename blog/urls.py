from django.conf.urls import include, url
from . import views

# as duas linhas acima importa métodos do Django e todos os nossos views do aplicativo blog

urlpatterns = [
    url(r'^$', views.post_list), #URL padrão
    #Essa expressão regular corresponderá a ^ (um começo) seguido por $ (fim)
    # então somente uma seqüência vazia irá corresponder.

    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    #r'^post/ :após o começo, da URL deve ter a palavra post e /
    #(?P<pk>[0-9]+):o Django vai levar tudo que você colocar aqui e transferir para uma view como uma variável chamada pk. [0-9] também nos diz que só pode ser um número, não uma letra (tudo entre 0 e 9). + significa que precisa existir um ou mais dígitos.
    # $: fim

    #Isso significa que se você digitar http://127.0.0.1:8000/post/5/ em seu navegador, Django vai entender que você está procurando uma view chamada post_detail e transferir a informação de que pk é igual a 5 para aquela view.
    #pk é uma abreviação para primary key (chave primária)

    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),

]
