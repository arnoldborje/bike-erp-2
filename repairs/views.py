from django.shortcuts import render, redirect, get_object_or_404
from .models import Repair
from .forms import RepairForm
from django.contrib.auth.decorators import login_required
from decorator.check_role import role_required


@login_required
@role_required(allowed_roles=['admin', 'mechanic'])
def repair_list_page(request):
    repairs = Repair.objects.select_related('bike').all()
    
    return render(request, 'repairs/list.html', {'repairs': repairs})


@login_required
@role_required(allowed_roles=['admin', 'mechanic'])
def repair_detail_page(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    return render(request, 'repairs/detail.html')


@login_required
@role_required(allowed_roles=['admin', 'mechanic'])
def repair_add_page(request):
    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('repair_list_page')
    else:
        form = RepairForm()
    return render(request, 'repairs/add.html', {'form': form})


@login_required
@role_required(allowed_roles=['admin', 'mechanic'])
def repair_edit_page(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    if request.method == 'POST':
        form = RepairForm(request.POST, instance=repair)
        if form.is_valid():
            form.save()
            return redirect('repair_list_page')
    else:
        form = RepairForm(instance=repair)
    
    return render(request, 'repairs/edit.html', {'form': form, 'repair': repair})
    

@login_required
@role_required(allowed_roles=['admin', 'mechanic'])
def repair_delete_page(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    if request.method == 'POST':
        repair.delete()
        return redirect('repair_list_page')
    return render(request, 'repairs/delete.html', {'repair': repair})
