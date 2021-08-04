from django.urls import path
from . import views
# each page path to be added below as it will refer to this file
urlpatterns = [
	path('', views.home, name="home"),
	path('about', views.about, name="about"),
	path('add_stock.html', views.add_stock, name="add_stock"),
	path('delete_stock.html', views.delete_stock, name="delete_stock"),
	path('delete/<stock_id>', views.delete, name="delete")
]