from django.shortcuts import render
from django.shortcuts import redirect
from .models import Pessoa

# Create your views here.
def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, "home.html", {"pessoas":pessoas})

def cadastrar_pessoa(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        Pessoa.objects.create(nome=nome, email=email, cpf=cpf)
        return redirect('home')
    return render(request, 'cadastrar.html')

def alterar_pessoa(request, id_pessoa):
    pessoa = Pessoa.objects.get(id_pessoa=id_pessoa)
    if request.method == 'POST':
        pessoa.nome = request.POST.get('nome')
        pessoa.email = request.POST.get('email')
        pessoa.cpf = request.POST.get('cpf')
        pessoa.save()
        return redirect('home')
    return render(request, "alterar.html", {"pessoa": pessoa})

def excluir_pessoa(request, id_pessoa):
    pessoa = Pessoa.objects.get(id_pessoa=id_pessoa)
    pessoa.delete()
    return redirect('home')

def pesquisar_pessoa(request):
    query = request.GET.get('input_pesquisar_pessoa', '')
    pessoas = Pessoa.objects.filter(nome__icontains=query)
    return render(request, 'home.html', {'pessoas':pessoas, 'query':query})