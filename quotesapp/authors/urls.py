from django.urls import path
from . import views


app_name = 'authors'

urlpatterns = [
    path('add-author/', views.add_author, name='add_author'),
    path('author/delete/<int:author_id>/', views.delete_author, name='delete_author'),
]