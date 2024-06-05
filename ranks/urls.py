from . import views
from django.urls import path , include

app_name = 'ranks'

urlpatterns = [
    path('', views.index , name = 'index'),
    path('physics', views.physics , name = 'physics'),
]