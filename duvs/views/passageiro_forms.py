from django.shortcuts import get_object_or_404,redirect,render
from duvs.forms import PassageiroForm
from django.urls import reverse
from duvs.models import Passageiro
from django.contrib import messages

def passageiro_create(request):
    form_action = reverse("duvs:passageiro_create")
    duv_id = request.GET.get('duv')
    if request.method == 'POST':
        form = PassageiroForm(request.POST, request.FILES)
        context = {
            'form': form,
            "form_action": form_action,
        }
        if form.is_valid():
            passageiro = form.save()
            messages.success(request, f'Passageiro {passageiro.nome} criado com sucesso!')
            return redirect(to='duvs:home')
        return render(request, template_name='duvs/passageiro_form.html', context=context)
    
    initial_data = {}
    if duv_id:
        initial_data['duv'] = duv_id
    
    form = PassageiroForm(initial=initial_data)
    context = {
        "form": PassageiroForm(),
        "form_action": form_action,
    }
    return render(request, template_name='duvs/passageiro_form.html', context=context)

def passageiro_update(request, passageiro_id):
    passageiro = get_object_or_404(Passageiro, pk=passageiro_id)
    form_action = reverse("duvs:passageiro_update", args=[passageiro.pk])
    if request.method == 'POST':
        form = PassageiroForm(request.POST, request.FILES,instance=passageiro)
        context = {
            'form': form,
            "form_action": form_action,
        }
        if form.is_valid():
            passageiro = form.save()
            messages.success(request, f'Passageiro {passageiro.nome} atualizado com sucesso!')
            return redirect(to='duvs:home')
        return render(request, template_name='duvs/passageiro_form.html', context=context)
    context = {
        "form": PassageiroForm(instance=passageiro),
        "form_action": form_action,
    }
    return render(
        request,
        template_name='duvs/passageiro_form.html',
        context=context
    )
def passageiro_delete(request, passageiro_id):
    passageiro = get_object_or_404(Passageiro, pk=passageiro_id)
    if request.method == "POST":
        confirmation = request.POST.get('confirmation', 'no')
        if confirmation == "yes":
            passageiro.delete()
            messages.success(request, f'Passageiro {passageiro.nome} deletado com sucesso!')
            return redirect(to='duvs:home')
    else:
        confirmation = request.GET.get('confirmation', 'no')
    return render(
        request,
        template_name='duvs/passageiro.html',
        context={"passageiro": passageiro, "confirmation": confirmation}
    )