from django.urls import path
from .views import index, confirmacionenvio, vertemario

urlpatterns = [
    path('', index, name="index"),
    path('envio/', confirmacionenvio),
    path('temario/<int:id>/', vertemario, name='temario')
]
