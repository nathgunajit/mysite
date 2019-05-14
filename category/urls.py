from django.urls import path, include
from django.conf.urls import url
from category import views
app_name='category'
urlpatterns = [
    path('', views.listing, name="listing"),
    path('<int:id>/', views.details, name="details"),
]

#path('favourite', include([
#    path('', views.listing, name="listing"),
#    path('<int:id>/', views.details, name="details"),

#]));
