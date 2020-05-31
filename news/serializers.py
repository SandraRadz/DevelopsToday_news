from rest_framework import serializers
from news.models import NewPost, Comment


class PostSerializer(serializers.ModelSerializer):
    upvotes_amount = serializers.ReadOnlyField()

    class Meta:
        model = NewPost
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
