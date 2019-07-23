from django.urls import path

from . import views

urlpatterns = [
	path('', views.bloggy, name='bloggy'),
	path('<int:blog_id>/', views.detail, name='detail'),
]