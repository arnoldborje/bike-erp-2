from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from decorator.check_role import role_required
from .models import Sale
from .forms import SaleForm
from .utils import send_mailjet_email
from django.contrib.auth.decorators import login_required

@login_required
@role_required(['sales', 'admin'])
def sale_list_page(request):
    sales = Sale.objects.all()
    return render(request, "sales/list.html", {"sales": sales})


@login_required
@role_required(['sales', 'admin'])
def sale_detail_page(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    return render(request, "sales/detail.html", {"sale": sale})


@login_required
@role_required(['sales', 'admin'])
def sale_add_page(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.sold_by = request.user
            sale.save()
            # also update bike status to SOLD
            sale.bike.status = "sold"

            sale.bike.save()

            send_mailjet_email(to_email=form.cleaned_data['customer_email'], to_name=form.cleaned_data['customer_name'], sale=sale)
            
            return redirect("sale_list_page")
    else:
        form = SaleForm()
    return render(request, "sales/add.html", {"form": form})   