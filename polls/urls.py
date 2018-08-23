from django.urls import path
from django.contrib import admin
from . import views # . means from this directory, import views (from view.py)

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/result/', views.result, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/detail', views.detail, name='detail')
]

#when http request comes to this URL pattern, view.result method is called, with http request and
# int:question_id in the parameters.

