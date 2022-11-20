from django.urls import path, re_path

from feedback import views

app_name = 'feedback'
urlpatterns = [
    path('', views.feedback, name='feedback'),
]
