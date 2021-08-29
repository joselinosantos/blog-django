from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages

def index(request):
	return render(request, 'posts/index.html')

def posts(request):
	search = request.GET.get('search')
	if search:
		posts = Post.objects.filter(titulo__icontains=search)
	else:
		posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
	return render(request, 'posts/posts.html', {'posts': posts})

def post(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/post.html', {'post': post})

def novo_post(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			post.data_publicacao = timezone.now()
			post.save()
			return redirect('/posts')
	else:
		form = PostForm()
	return render(request, 'posts/post_new.html', {'form': form})

def edit_post(request, id):
	post = get_object_or_404(Post, pk=id)
	form = PostForm(instance=post)

	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			post.data_publicacao = timezone.now()
			post.save()
			return redirect('posts')
		else:
			return render(request, 'posts/post_edit.html', {'form': form, 'post':post})
	else:
		return render(request, 'posts/post_edit.html', {'form': form, 'post':post})

def delete_post(request, id):
	post = get_object_or_404(Post, pk=id)
	post.delete()
	messages.info(request, 'Post deletado')
	return redirect('/posts')