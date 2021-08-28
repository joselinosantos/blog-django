from django.urls import path
from blog import views as views_blog
from perfil import views as views_perfil

urlpatterns = [
	path('', views_blog.index, name='index'),
	path('posts/', views_blog.posts, name='posts'),
	path('post/<int:id>/', views_blog.post, name='post'),
	path('post/novo/', views_blog.novo_post, name='novo-post'),
	path('post/<int:id>/edit/', views_blog.edit_post, name='edit-post'),
	path('post/<int:id>/delete/', views_blog.delete_post, name='delete-post'),
	path('quem_sou', views_perfil.quem_sou, name='quem_sou'),
]