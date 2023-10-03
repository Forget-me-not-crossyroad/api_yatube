from pyparsing import Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import serializers
import datetime as dt

from posts.models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())
    # group = serializers.PrimaryKeyRelatedField(read_only=True)

    # achievements = AchievementSerializer(many=True, required=False)
    # age = serializers.SerializerMethodField()
    # color = serializers.ChoiceField(choices=CHOICES)

    class Meta:
        model = Post
        # fields = '__all__'
        fields = ('id', 'text', 'pub_date', 'image', 'author', 'group')

    # def get_age(self, obj):
    #     return dt.datetime.now().year - obj.birth_year

    # def create(self, validated_data):
    #     # Если в исходном запросе не было поля achievements
    #     if 'achievements' not in self.initial_data:
    #         # То создаём запись о котике без его достижений
    #         cat = Cat.objects.create(**validated_data)
    #         return cat

    #     # Иначе делаем следующее:
    #     # Уберём список достижений из словаря validated_data и сохраним его
    #     achievements = validated_data.pop('achievements')
    #     # Сначала добавляем котика в БД
    #     cat = Cat.objects.create(**validated_data)
    #     # А потом добавляем его достижения в БД
    #     for achievement in achievements:
    #         current_achievement, status = Achievement.objects.get_or_create(
    #             **achievement)
    #         # И связываем каждое достижение с этим котиком
    #         AchievementCat.objects.create(
    #             achievement=current_achievement, cat=cat)
    #     return cat


class GroupSerializer(serializers.ModelSerializer):
    # achievements = AchievementSerializer(many=True, required=False)
    # age = serializers.SerializerMethodField()
    # color = serializers.ChoiceField(choices=CHOICES)

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class GroupRetrieveSerializer(serializers.ModelSerializer):
    # achievements = AchievementSerializer(many=True, required=False)
    # age = serializers.SerializerMethodField()
    # color = serializers.ChoiceField(choices=CHOICES)

    class Meta:
        model = Group
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Post
        fields = ('__all__')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())
    post = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'text', 'created', 'author', 'post')

    def get_post(self, obj):
        return obj.post.id