from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm
from datetime import date
from django.utils import timezone
from django.db.models import Count
from django.http import HttpResponse
from datetime import datetime, timedelta
import os
# Create your views here.




def listar (request):
	lista0 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CADASTRADO, acao=Aluno.VOLTA)
	lista1 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CADASTRADO, acao=Aluno.IDA)
	lista2 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CARONA,acao=Aluno.VOLTA)
	lista3 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CARONA,acao=Aluno.IDA)
	lista4 = Aluno.objects.all().order_by('data').filter(acao=Aluno.IDA)
	lista5 = Aluno.objects.all().filter(acao=Aluno.VOLTA)
	aux=0
	aux2=0
	cor="success"
	classe='smile'
	for x in lista4:
		aux = aux+1
	for y in lista5:
		aux2 = aux2+1
	
	if aux==40 or aux2==40:
		cor="warning"
		classe='grimace'
	if aux>40:
		cor="danger"
		classe='frown'
	if aux2>40:
		cor="danger"
		classe='frown'
	
	p='pessoas'
	p2='pessoas'
	if aux==1:
		p='pessoa'
	if aux2==1:
		p2='pessoa'
	return render (request, 'main.html', {'pessoa':p,'pessoa2':p2,'classe':classe,'cor':cor,'totali':aux, 'totalv':aux2,"cadastrados": lista0,'caronas': lista2, 'cadastradosi':lista1, 'caronasi':lista3})	

def tirar(request, id):
	aux2=id
	#cod=cod	
	try:
		aux = Aluno.objects.get(id=id)
		print(aux.cod)
		codigo =  request.POST['confirmacod']
		
		if aux.cod == codigo:
			aux.delete()
			return redirect('menu')

		lista0 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CADASTRADO, acao=Aluno.VOLTA)
		lista1 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CADASTRADO, acao=Aluno.IDA)
		lista2 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CARONA,acao=Aluno.VOLTA)
		lista3 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CARONA,acao=Aluno.IDA)
		return render(request, 'main.html',{'alertacoderro':'ok', "cadastrados": lista0,'caronas': lista2, 'cadastradosi':lista1, 'caronasi':lista3})
			
	except :
		return redirect('menu')


def novalista(request):
	data_e_hora_atuais = datetime.now()
	hora = data_e_hora_atuais.strftime('%H')#o %H retorna apenas a hora
	hora1=int(hora)
	try:
		if hora1 == 19:	
			aux = Aluno.objects.all()
			aux.delete()
			return redirect('menu')
	except :
		return redirect('menu')
	lista0 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CADASTRADO, acao=Aluno.VOLTA)
	lista1 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CADASTRADO, acao=Aluno.IDA)
	lista2 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CARONA,acao=Aluno.VOLTA)
	lista3 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CARONA,acao=Aluno.IDA)
	return render(request, 'main.html',{'alerta2':'ok', "cadastrados": lista0,'caronas': lista2, 'cadastradosi':lista1, 'caronasi':lista3})
	
def novalista1(request):
	
	senha =  request.POST['senha']
	try:
		if senha == '@galego321':
			aux = Aluno.objects.all()
			aux.delete()
			return redirect('menu')

	except :
		return redirect('menu')
	lista0 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CADASTRADO, acao=Aluno.VOLTA)
	lista1 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CADASTRADO, acao=Aluno.IDA)
	lista2 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CARONA,acao=Aluno.VOLTA)
	lista3 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CARONA,acao=Aluno.IDA)
	return render(request, 'main.html',{'alertasenha':'ok', "cadastrados": lista0,'caronas': lista2, 'cadastradosi':lista1, 'caronasi':lista3})
	


def cadastrar(request):
	if request.method =='POST':
		#formularioReclamacao = Reclamacao(request.POST)
		#if formularioReclamacao.is_valid():
		
		#if nome == 'admin':
		#    return render(request, 'aluno/login.html', {'alerta3': 'Erro'})
		data_atual = date.today()
		data_e_hora_atuais = datetime.now()
		hora = data_e_hora_atuais.strftime('%H')#o %H retorna apenas a hora
		hora1=int(hora)
		
		nome = request.POST['nome']
		acao = request.POST['acao']
		instituicao = request.POST['instituicao']
		situacao = request.POST['situacao']
		codigo = request.POST['cod']
		
		lista0 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CADASTRADO, acao=Aluno.VOLTA)
		lista1 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CADASTRADO, acao=Aluno.IDA)
		lista2 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CARONA,acao=Aluno.VOLTA)
		lista3 = Aluno.objects.all().order_by('data').filter(situacao=Aluno.CARONA,acao=Aluno.IDA)
		listav = Aluno.objects.all().filter(acao=Aluno.VOLTA)
		listai = Aluno.objects.all().filter(acao=Aluno.IDA)
		if acao =="1":	
			for i in listai:
				if nome == i.nome:
					return render(request, 'main.html',{'alertanomeexistente':'ok', "cadastrados": lista0,'caronas': lista2, 'cadastradosi':lista1, 'caronasi':lista3})
		if acao =="3":
			for v in listav:
				if nome == v.nome:
					return render(request, 'main.html',{'alertanomeexistente':'ok', "cadastrados": lista0,'caronas': lista2, 'cadastradosi':lista1, 'caronasi':lista3})
		if acao =="2":
			for i in listai:
				if nome == i.nome:
					return render(request, 'main.html',{'alertanomeexistente':'ok', "cadastrados": lista0,'caronas': lista2, 'cadastradosi':lista1, 'caronasi':lista3})
			for v in listav:
				if nome == v.nome:
					return render(request, 'main.html',{'alertanomeexistente':'ok', "cadastrados": lista0,'caronas': lista2, 'cadastradosi':lista1, 'caronasi':lista3})
			



		if hora1 == 19:
			
			return render(request, 'main.html',{'alerta3':'ok', "cadastrados": lista0,'caronas': lista2, 'cadastradosi':lista1, 'caronasi':lista3})

		if 10 <= hora1 <= 18:
			
			if acao=='2':
				Aluno.objects.create(nome=nome, acao='1', instituicao=instituicao, situacao='2', cod=codigo)
				Aluno.objects.create(nome=nome, acao='3', instituicao=instituicao, situacao='2', cod=codigo)
				if situacao=='1':
					return render(request, 'main.html',{'alerta':'ok', "cadastrados": lista0,'caronas': lista2, 'cadastradosi':lista1, 'caronasi':lista3})
				return redirect('menu')

			Aluno.objects.create(nome=nome, acao=acao, instituicao=instituicao, situacao='2', cod=codigo)
			if situacao=='1':
				return render(request, 'main.html',{'alerta':'ok', "cadastrados": lista0,'caronas': lista2, 'cadastradosi':lista1, 'caronasi':lista3})
			
			return redirect('menu')


		if acao=='2':
			Aluno.objects.create(nome=nome, acao='1', instituicao=instituicao, situacao=situacao, cod=codigo)
			Aluno.objects.create(nome=nome, acao='3', instituicao=instituicao, situacao=situacao, cod=codigo)
			return redirect('menu')
			
		Aluno.objects.create(nome=nome, acao=acao, instituicao=instituicao, situacao=situacao, cod=codigo)

		return redirect('menu')
	

