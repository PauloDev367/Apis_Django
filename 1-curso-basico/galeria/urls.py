from django.urls import path
from galeria.views import index

# boa prática
urlpatterns = [
    path("", index)
]