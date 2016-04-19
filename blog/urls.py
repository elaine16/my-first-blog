from django.conf.urls import include, url
from . import views

# as duas linhas acima importa métodos do Django e todos os nossos views do aplicativo blog

urlpatterns = [
    url(r'^$', views.post_list), #URL padrão
    #Essa expressão regular corresponderá a ^ (um começo) seguido por $ (fim)
    # então somente uma seqüência vazia irá corresponder.
]
