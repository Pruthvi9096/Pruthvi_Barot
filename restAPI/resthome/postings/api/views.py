from rest_framework import generics
from postings.models import BlogPost
from .serializers import BlogPostSerializer

#Detail View
class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer
    # queryset = BlogPost.objects.all()

    def get_queryset(self):
        return BlogPost.objects.all()

