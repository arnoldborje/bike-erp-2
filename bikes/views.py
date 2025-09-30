from django.forms import BaseForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Bike
from .forms import BikeForm
from django.contrib.auth.decorators import login_required



@login_required
def bike_list_page(request):
    bikes = Bike.objects.all()
    
    return render(request, 'bike/list.html', { "bikes": bikes })


@login_required
def bike_detail_page(request, pk):
    bike = get_object_or_404(Bike, pk=pk)

    return render(request, 'bike/detail.html', { 'bike': bike })


@login_required
def bike_add_page(request):
    if request.method == "POST":
        form = BikeForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('bike_list_page')
        else:
            print(form.errors)
    else:
        form = BikeForm()
    
    return render(request, 'bike/add.html', {'form': form})


@login_required
def bike_edit_page(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    if request.method == "POST":
        form = BikeForm(request.POST, request.FILES, instance=bike)
        if form.is_valid():
            form.save()
            return redirect("bike_list_page")
        else:
            print(form.errors)
    else:
        form = BikeForm(instance=bike)
    
    return render(request, 'bike/edit.html', { "form": form })


@login_required
def bike_delete_page(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    bike.delete()
    return redirect("bike_list_page")