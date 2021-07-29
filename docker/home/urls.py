from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='home-index'),
   path('cv/', views.cv_page, name='cv-page'),
   path('learn-html', views.learn_html)
]