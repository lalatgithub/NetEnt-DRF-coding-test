from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import *


class BookSerializer(serializers.ModelSerializer):

    author = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Book
        fields = ('title', 'published_at', 'genres', 'author')
        validators = [
            UniqueTogetherValidator(
                queryset=Book.objects.all(),
                fields=('title', 'author'),
                message='You have already published a Book with same title.'
            )
        ]

    def validate(self, attrs):
        author_books_count = Book.objects.filter(author=attrs.get('author')).count()
        if not self.instance and author_books_count >= 5:
            raise serializers.ValidationError('An author is only allowed to have 5 books at one time')
        return attrs


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
