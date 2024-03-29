from django.urls import path
from posts import views as views_posts
from perfil import views as views_perfil

urlpatterns = [
	path('', views_posts.index, name='index'),
	path('posts/', views_posts.posts, name='posts'),
	path('post/<int:id>/', views_posts.post, name='post'),
	path('novo/', views_posts.novo_post, name='novo-post'),
	path('edit/<int:id>', views_posts.edit_post, name='edit-post'),
	path('delete/<int:id>', views_posts.delete_post, name='delete-post'),
	path('quem_sou', views_perfil.quem_sou, name='quem_sou'),
]