from django.urls import path
from . import views
app_name = 'post'
urlpatterns = [
    path('postlist/', views.post_list, name="postlist"),
    path('posts/<int:id>/', views.post_details, name="postdetails"),
]
