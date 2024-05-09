from django.urls import path
from listatarefas.views import index

urlpatterns = [
    path('', index)
]