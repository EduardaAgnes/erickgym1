
from django.contrib import admin
from django.urls import path
from exercicios.views import DetailUpdateDeleteAlunos, ListCreateAlunos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exercicios/', ListCreateAlunos.as_view()),
    path('exercicios/<int:pk>', DetailUpdateDeleteAlunos.as_view()),
]