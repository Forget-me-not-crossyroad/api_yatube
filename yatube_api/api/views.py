from rest_framework import viewsets
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer, PostListSerializer

from posts.models import Comment, Post, Group


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

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


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset
