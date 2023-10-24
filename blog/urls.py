from django.urls import path
from .views import post_detail, post_list, PostList

app_name='blog'

urlpatterns = [
    #path('post_list/', post_list, name='post-list'),
    path('post_list/', PostList.as_view(), name='post-list'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>', post_detail, name='post-detail'),
]