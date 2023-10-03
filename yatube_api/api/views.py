import os
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer, PostListSerializer

from posts.models import Comment, Post, Group
from django.core.exceptions import PermissionDenied


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        filepath = f'{settings.MEDIA_ROOT}/{instance.image.name}'
        if os.path.exists(filepath):
            os.remove(filepath)
        instance.delete()

    # def perform_destroy(self, serializer):
    #     if serializer.instance.author != self.request.user:
    #         raise PermissionDenied('Изменение чужого контента запрещено!')
    #     super(PostViewSet, self).perform_destroy(serializer)
    # Пишем метод, а в декораторе разрешим работу со списком объектов
    # и переопределим URL на более презентабельный
    # @action(detail=False, url_path='recent-white-cats')
    # def recent_white_cats(self, request):
    #     # Нужны только последние пять котиков белого цвета
    #     cats = Cat.objects.filter(color='White')[:5]
    #     # Передадим queryset cats сериализатору 
    #     # и разрешим работу со списком объектов
    #     serializer = self.get_serializer(cats, many=True)
    #     return Response(serializer.data)

    # def get_serializer_class(self):
    #     # Если запрошенное действие (action) — получение списка объектов ('list')
    #     if self.action == 'list':
    #         # ...то применяем CatListSerializer
    #         return PostListSerializer
    #     # А если запрошенное действие — не 'list', применяем CatSerializer
    #     return PostSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        serializer.save(post=post)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        instance.delete()

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return PostListSerializer
    #     return GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        return post.comments.all()
    
    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        instance.delete()
