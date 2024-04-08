from django.urls import path
from galeria.views import index, imagem

# boa prática
urlpatterns = [
    path("", index),
    path("imagem", imagem, name='imagem'),
]