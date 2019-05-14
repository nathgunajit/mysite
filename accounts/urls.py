from django.urls import path
from accounts import views
app_name="accounts"
urlpatterns = [
    path('login/', views.user_login, name="user_login"),
    path('success/', views.success, name='user_success'),
    path('logout/', views.user_logout, name='user_logout'),
    path('', views.user_home, name='user_home'),
]
