from django.urls import path
from . import views

app_name = 'SearchApp'

urlpatterns = [
	path('',views.index,name='index'),

	path('ajax_calls/search/', views.autocompleteBook,name = 'autocompleteBook'),

	
	
]