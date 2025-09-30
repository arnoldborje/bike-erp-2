from django.shortcuts import render
from django.db.models import Count, Sum
from bikes.models import Bike
from sales.models import Sale
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_page(request):
    # List of sales
    sales_list = Sale.objects.all()
    
    # Total bikes
    total_bikes = Bike.objects.count()

    # Bikes ready for sale
    bikes_ready_for_sale = Bike.objects.filter(status="ready_to_sell").count()

    # Bikes under repair
    bikes_under_repair = Bike.objects.filter(status="for_repair").count()

    # Bikes sold
    bikes_sold = Bike.objects.filter(status="sold").count()
    
    # Total sales revenue
    total_sales = Sale.objects.aggregate(total=Sum('selling_price'))['total'] or 0
    
    # Total profit (assuming profit is selling_price - ( purchase_price + repair_cost))
    total_profit = 0
    
    for sale in sales_list:
        total_profit += (sale.selling_price - sale.bike.total_cost)



    context = {
        'total_bikes': total_bikes,
        'bikes_ready_for_sale': bikes_ready_for_sale,
        'bikes_under_repair': bikes_under_repair,
        'bikes_sold': bikes_sold,
        'total_sales': total_sales,
        'profit': total_profit,
        'sales_list': sales_list,
    }

    print(f"Total Bikes: {total_bikes}")
    print(f"Bikes Under Repair: {bikes_under_repair}")
    print(f"Bikes Sold: {bikes_sold}")
    print(f"Total Sales Revenue: {total_sales}")
    print(f"Total Profit: {total_profit}")

    return render(request, 'dashboard/dashboard.html', context)