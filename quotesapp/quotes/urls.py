from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path("", views.main, name='main'),
    path("tags/<slug:tag_name>/", views.quotes_by_tag_view, name='quotes_by_tag'),
    path("author/<int:author_id>/", views.author_detail, name='author_detail'),
    path("add-quote/", views.add_quote, name="add_quote"),
    path("add_tag/", views.add_tag, name="add_tag"),
    path('quote/delete/<int:quote_id>/', views.delete_quote, name='delete_quote'),
]