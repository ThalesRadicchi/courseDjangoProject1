from django.urls import path
from recipes.views import home, about, contact

urlpatterns = [
    path("", home), #Home
    path("sobre/", about), #/sobre/
    path("contato/", contact), #/contato/
]
