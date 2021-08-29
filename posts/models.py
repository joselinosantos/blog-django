from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
	CATEGORIAS = (
		('Python', 'Python'),
		('Raspberry Pi', 'Raspberry Pi'),
		('SQL', 'SQL'),
		('Web', 'Web'),
		('DataScience', 'DataScience')
	)
	titulo = models.CharField(max_length=200)
	autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	imagem = models.CharField(max_length=20)
	texto = models.TextField()
	categoria = models.CharField(max_length=12, choices=CATEGORIAS)
	data_criacao = models.DateTimeField(default=timezone.now)
	data_publicacao = models.DateTimeField(blank=True, null=True)

	def publicar(self):
		self.data_publicacao = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo