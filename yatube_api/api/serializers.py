from posts.models import Comment, Group, Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post.
    Поля:
    - id: ID поста (целое число).
    - text: Текст поста (строка).
    - author: Автор поста (только для чтения, строка - имя пользователя).
    - image: Изображение поста (строка - URL изображения).
    - group: Группа, к которой относится пост (целое число - ID группы).
    - pub_date: Дата публикации поста (дата и время).
    """
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'image', 'author', 'group')


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group.
    Поля:
    - id: ID группы (целое число).
    - title: Название группы (строка).
    - slug: Уникальный идентификатор группы (строка).
    - description: Описание группы (строка).
    """
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment.

    Поля:
    - id: ID комментария (целое число).
    - author: Автор комментария (только для чтения, строка - имя пользователя).
    - post: Пост, к которому относится комментарий (целое число - ID поста).
    - text: Текст комментария (строка).
    - created: Дата создания комментария (дата и время).
    """
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )
    post = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'text', 'created', 'author', 'post')

    def get_post(self, obj):
        return obj.post.id
