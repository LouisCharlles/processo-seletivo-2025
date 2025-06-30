from django.shortcuts import get_object_or_404,redirect,render
from duvs.forms import NavioForm
from django.urls import reverse
from duvs.models import Navio
from django.contrib import messages

def navio_create(request):
    form_action = reverse("duvs:navio_create")
    if request.method == 'POST':
        form = NavioForm(request.POST, request.FILES)
        context = {
            'form': form,
            "form_action": form_action,
        }
        if form.is_valid():
            navio = form.save()
            messages.success(request, f'{navio.nome} criado com sucesso!')
            return redirect(to='duvs:home')
        return render(request, template_name='duvs/navio_form.html', context=context)
    context = {
        "form": NavioForm(),
        "form_action": form_action,
    }
    return render(request, template_name='duvs/navio_form.html', context=context)
def navio_update(request, navio_id):
    navio = get_object_or_404(Navio, pk=navio_id)
    form_action = reverse("duvs:navio_update", args=[navio.pk])
    if request.method == 'POST':
        form = NavioForm(request.POST,request.FILES, instance=navio)
        context = {
            'form': form,
            "form_action": form_action,
        }
        if form.is_valid():
            navio = form.save()
            messages.success(request, f'{navio.nome} atualizado com sucesso!')
            return redirect(to='duvs:home')
        return render(request, template_name='duvs/navio_form.html', context=context)
    context = {
        "form": NavioForm(instance=navio),
        "form_action": form_action,
    }
    return render(
    request, 
    template_name='duvs/navio_form.html',
    context=context
    )
def navio_delete(request, navio_id):
    navio = get_object_or_404(Navio, pk=navio_id)
    if request.method == "POST":
        confirmation = request.POST.get('confirmation', 'no')
        if confirmation == "yes":
            navio.delete()
            messages.success(request, f'{navio.nome} deletado com sucesso!')
            return redirect(to='duvs:home')
    return render(
        request,
        template_name='duvs/navio.html',
        context={"navio": navio, "confirmation": confirmation}
    )
