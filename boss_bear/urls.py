from django.urls import path
from . import views

app_name = 'bears'
urlpatterns = [
    path('', views.EmployeeFormView.as_view(), name='index'),
    path('register', views.register, name='register')
]