from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
	url('(?P<pk>[0-9]+)/results/', views.ResultsView.as_view(), name = 'results'),
	url('(?P<qid>[0-9]+)/vote/', views.vote, name = 'vote'),
	url('(?P<pk>[0-9]+)/', views.DetailView.as_view(), name = 'detail'),
	url('', views.IndexView.as_view(), name = 'index'),
	
]