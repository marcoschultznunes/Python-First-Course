"""
    We define patch in the update API view
"""
class PostUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostUpdateSerializer

    def patch(self, request, pk):
        post = get_object_or_404(Post, pk=pk) # imported from django.shortcuts
        serializer = PostUpdateSerializer(post, data=request.data, partial=True, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) # imported from rest_framework.response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
    Note: You must send raw json data instead of using an html form to send a patch request.
"""
