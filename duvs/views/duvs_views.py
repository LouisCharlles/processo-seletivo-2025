from django.shortcuts import render, get_object_or_404, redirect
from duvs.models import DUV,Passageiro,Navio
from django.db.models import Q

from django.core.paginator import Paginator

def home(request):
    duvs = DUV.objects.all().order_by('-data_viagem')
    paginator = Paginator(duvs, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'site_title': "Home - "
    }
    return render(
        request,
        template_name='duvs/index.html',
        context=context,
    )

def search(request):
    search_value = request.GET.get("q","").strip()
    duvs = DUV.objects \
        .filter(
            Q(numero__icontains=search_value)
        )\
        .order_by('-id')
    
    paginator = Paginator(duvs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj":page_obj,
        "site_title":"Buscado - ",
        "search_value":search_value,
    }
    if search_value=="":
        redirect("duvs:home")
    
    return render(
        request,
        template_name="duvs/index.html",
        context=context,
    )
def get_duv(request,duv_id:int):
    single_duv = get_object_or_404(DUV.objects, pk=duv_id)
    context = {
        'duv': single_duv,
        'site_title': single_duv.numero
    }
    return render(
        request,
        template_name='duvs/duv.html',
        context=context
    )

def passageiro_detail(request, passageiro_id):
    passageiro = get_object_or_404(Passageiro, pk=passageiro_id)
    return render(
        request,
        template_name='duvs/passageiro.html',
        context={
            'passageiro': passageiro,
            'site_title': f'Passageiro {passageiro.nome}'
        }
    )

def passageiro_search(request):
    search_value = request.GET.get("q", "").strip()
    passageiros = Passageiro.objects.filter(
        Q(nome__icontains=search_value)
    ).order_by('-id')

    paginator = Paginator(passageiros, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "site_title": f"Busca Passageiro - {search_value}",
        "search_value": search_value,
    }

    return render(
        request,
        "duvs/passageiro_search.html",
        context
    )
def navio_detail(request, navio_id):
    navio = get_object_or_404(Navio, pk=navio_id)
    context = {
        'navio': navio,
        'site_title': f'Navio {navio.nome}'
    }
    return render(
        request,
        template_name='duvs/navio.html',
        context=context
    )