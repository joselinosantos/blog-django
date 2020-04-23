from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Função para as views
def post_list(request):
	posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
	return render(request, 'blog/post_list.html', {'posts': posts})
	#Post.objects.get(pk=pk)

def post_detalhes(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detalhes.html', {'post': post})
