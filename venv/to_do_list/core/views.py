from django.shortcuts import render, HttpResponse
from .models import AtividadeModel
import datetime
from .forms import AtividadeModelForm
from django.shortcuts import redirect

data = datetime.date.today()

#função para consultar
def index(request):
    lista=[]
    context={'lista':lista}
    lista=AtividadeModel.objects.all()
    
    for item in lista:
        if item.data == data:
            context['lista'].append(item)
            
    return render(request,'index.html', context)


#função para cadastrar atividade
def cadastro(request):
    if request.method == 'POST':

        form = AtividadeModelForm(request.POST)

        if form.is_valid():
            nome=form.data['nome']
            tipo=form.data['tipo']
            descricao=form.data['descricao']
            data=form.data['data']
                
            form.save()
            return index(request)
        return HttpResponse('Erro de cadastro')
    else:

        contexto = {'form': AtividadeModelForm() }    
        return render(request,'cadastro.html', contexto)

from django.shortcuts import get_object_or_404, redirect


# função para deletar atividade
def deletar(request):
    if request.method == 'POST': #essa linha valida se esta recebendo via post
        id = request.POST.get('id')  # pega o id recebido via post de deletar.html

        try:
            atividade = AtividadeModel.objects.get(id=id)
            atividade.delete()
            return redirect('deletar')  # Redireciona para a página deletar após a exclusão
        except AtividadeModel.DoesNotExist: #caso não tenha o id ele entra nesse tratamento de exceção 
            return HttpResponse('Atividade não encontrada')
    else: # se não estiver recebendo via post
        return render(request, 'deletar.html')
    
# função para fazer update
def atualizar(request):
    if request.method == 'POST':
        atividade_id = request.POST.get('id')
        atividade = AtividadeModel.objects.get(pk=atividade_id)
        
        atividade.nome = request.POST.get('nome')
        atividade.tipo = request.POST.get('tipo')
        atividade.descricao = request.POST.get('descricao')
        atividade.data = request.POST.get('data')
        
        atividade.save()
        
        return redirect('atualizar')
    else:
        return render(request, 'atualizar.html', {'atividade': None})

    
        
