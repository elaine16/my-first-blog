from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'siteblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), #para cada URL que começa com admin / o Django irá encontrar um correspondente modo de exibição.
    url(r'', include('blog.urls')), # vai importar blog.urls para a url principal ('').
]

#O Django agora irá redirecionar tudo o que entra em 'http://127.0.0.1:8000 /'para blog.urls e procurar por novas instruções lá.