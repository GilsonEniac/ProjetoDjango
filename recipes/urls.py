from django.urls import path

from recipes.views import home, sobre, contato, info, detalhe


urlpatterns = [
    path('', home), # Home
    path('sobre/', sobre), #/sobre
    path('contato/', contato), #/Contato
    path('info/', info), #/info
    path('info/detalhe/', detalhe)
]