from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from news.models import NewPost
from news.serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = NewPost.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewPost.objects.all()
    serializer_class = PostSerializer


@api_view(["PUT"])
def upvote_new(request, pk):
    post = get_object_or_404(NewPost, pk=pk)
    post.upvotes_amount += 1
    post.save()
    serializer = PostSerializer(post)
    return Response(serializer.data)

