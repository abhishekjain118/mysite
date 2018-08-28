from django.urls import path
from django.contrib import admin
from . import views # . means from this directory, import views (from view.py)

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/result/', views.ResultView.as_view(), name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail')
]
## int:pk is required by the generic views.

#when http request comes to this URL pattern, view.result method is called, with http request and
# int:question_id in the parameters.

