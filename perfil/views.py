from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def quem_sou(request):
	return render(request, 'perfil/quem_sou.html')