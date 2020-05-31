from django.urls import path

from news.views import PostList, PostDetail, upvote_new

urlpatterns = [
    path('', PostList.as_view(), name="post-list"),
    path('<int:pk>/', PostDetail.as_view(), name="post-detail"),
    path('<int:pk>/upvote', upvote_new, name="upvote-new")
]