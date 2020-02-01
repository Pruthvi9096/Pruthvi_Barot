from rest_framework import serializers,permissions
from snippet_test.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from snippet_test.permissions import IsOwnerOrReadOnly

class SnippetSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Snippet
		fields = ['id', 'title', 'code', 'linenos', 'language', 'style','owner']
		permissions_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class UserSerializer(serializers.ModelSerializer):
	snippets = serializers.PrimaryKeyRelatedField(many=True,queryset=Snippet.objects.all())

	class meta:
		model = User
		fields = ['id','username','snippets']
		permissions_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
