from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

def index(request):
	return render(request, 'blog/index.html')

def posts(request):
	search = request.GET.get('search')
	if search:
		posts = Post.objects.filter(titulo__icontains=search)
	else:
		posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
	return render(request, 'blog/posts.html', {'posts': posts})
'''
def posts(request):
	posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
	return render(request, 'blog/post_list.html', {'posts': posts})
'''
def post(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/post.html', {'post': post})

def novo_post(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			post.data_publicacao = timezone.now()
			post.save()
			return redirect('post', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/novo_post.html', {'form': form})

def edit_post(request, id):
	post = get_object_or_404(Post, pk=id)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user # so funciona se tiver logado no admin
			post.data_publicacao = timezone.now()
			post.save()
			return redirect('post', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

def delete_post(request, id):
	if request.method == "POST":
		return 'Deletar'
	else:
		return 'Nao deletar'