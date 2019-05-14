from django.urls import path, include
from django.conf.urls import url
from accounts import views
app_name='accounts'
urlpatterns = [
    path('login/', views.login_view, name="login_view"),
    path('register/', views.register_view, name="register_view"),
    path('logout/', views.logout_view, name="logout_view"),
]