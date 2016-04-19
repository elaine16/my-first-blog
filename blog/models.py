from django.db import models
from django.utils import timezone


# class é uma palavra-chave especial que indica que estamos definindo um objeto.
# Post é o nome do nosso modelo, podemos lhe dar um nome diferente (mas é preciso evitar os espaços em branco e caracteres especiais). Sempre comece um nome de classe com uma letra maiúscula.
# models.Model significa que o Post é um modelo de Django, então o Django sabe ele que deve ser salvo no banco de dados.

class Post(models.Model):
    author = models.ForeignKey('auth.User') #models.ForeignKey - este é um link para outro modelo.
    title = models.CharField(max_length=200) #models.CharField: define um texto com um número limitado de caracteres.
    text = models.TextField() #models.TextField - este é para textos longos sem um limite.
    created_date = models.DateTimeField(
            default=timezone.now)    #models.DateTimeField - este é uma data e hora.
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): # def: é uma função publish: é o nome do método
        self.published_date = timezone.now()
        self.save()

    def __str__(self):  # quando chamamos __str__() teremos um texto (string), com um título do Post
        return self.title
