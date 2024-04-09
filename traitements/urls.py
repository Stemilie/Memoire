from django.urls import path
from . import views
urlpatterns=[
    path("",views.index, name='index3'),
    path('submit', views.submit_form, name= 'inscription'),
    path('authentification', views.index, name="authentification")
]
