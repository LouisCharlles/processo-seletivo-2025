from django.shortcuts import get_object_or_404,redirect,render
from duvs.forms import DuvForm
from django.urls import reverse
from duvs.models import DUV
from django.contrib import messages

def duv_create(request):
    form_action = reverse("duvs:duv_create")
    if request.method == 'POST':
        form = DuvForm(request.POST, request.FILES)
        context = {
            'form': form,
            "form_action": form_action,
        }
        if form.is_valid():
            duv = form.save()
            messages.success(request, f'{duv.numero} criada com sucesso!')
            # return redirect(reverse('duvs:duv_detail', args=[duv.pk]))
            return redirect(to='duvs:home')
        return render(request,template_name='duvs/duv_form.html',context=context)
    context = {
        "form":DuvForm(),
        "form_action": form_action,
    }
    return render(request, template_name='duvs/duv_form.html', context=context)

def duv_update(request,duv_id):
    duv = get_object_or_404(DUV, pk=duv_id)
    form_action = reverse("duvs:duv_update", args=[duv.pk])
    if request.method == 'POST':
        form = DuvForm(request.POST, instance=duv)
        context = {
            'form': form,
            "form_action": form_action,
        }
        if form.is_valid():
            duv = form.save()
            messages.success(request, f'{duv.numero} atualizada com sucesso!')
            return redirect(to='duvs:home')
        return render(request, template_name='duvs/duv_form.html', context=context)
    context = {
        "form": DuvForm(instance=duv),
        "form_action": form_action,
    }
    return render(
    request, 
    template_name='duvs/duv_form.html',
    context=context
    )

def duv_delete(request, duv_id):
    duv = get_object_or_404(DUV, pk=duv_id)
    if request.method == "POST":
        confirmation = request.POST.get('confirmation', 'no')
        if confirmation == "yes":
            duv.delete()
            messages.success(request, f'{duv.numero} deletada com sucesso!')
            return redirect(to='duvs:home')
    else:
        confirmation = request.GET.get('confirmation', 'no')
    
    return render(
        request,
        template_name='duvs/duv.html',
        context={
            'duv': duv,
            'confirmation': confirmation,
        }
    )
