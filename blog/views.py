from django.shortcuts import render
from .models import Post
from django.utils import timezone

# As views
def post_list(request):
	posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
	return render(request, 'blog/post_list.html', {'posts': posts})
	
