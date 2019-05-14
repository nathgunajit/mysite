from django.urls import path, include
from django.conf.urls import url
from request_user import views
app_name='request_user'
urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('form-register', views.formRegister, name="form_register"),
    path('listing/', views.listing, name="listing"),
    path('<int:id>/', views.details, name="details"),
]