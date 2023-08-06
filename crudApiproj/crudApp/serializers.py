from rest_framework import serializers
from crudApp.models import Post, Like

class PostSerializer(serializers.ModelSerializer):
    # like_count= serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    # def get_like_count(self,obj):
    #     return obj.like_set.count()

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


