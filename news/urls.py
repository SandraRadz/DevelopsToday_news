from django.urls import path

from news.views import PostList, PostDetail, upvote_new, CommentList, CommentDetail

urlpatterns = [
    path('', PostList.as_view(), name="post-list"),
    path('<int:pk>/', PostDetail.as_view(), name="post-detail"),
    path('<int:pk>/upvote', upvote_new, name="upvote-new"),
    path('comments', CommentList.as_view(), name="comment-list"),
    path('comments/<int:pk>/', CommentDetail.as_view(), name="comment-detail")
]