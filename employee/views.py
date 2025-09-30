from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required


@login_required
def employee_list_page(request):
    employees = Employee.objects.all()
    
    print(employees)
    return render(request, 'employees/list.html', {'employees': employees})



@login_required
def employee_add_page(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # Create User first
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
            )
            # Create Employee linked to User
            employee = form.save(commit=False)
            employee.user = user
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add.html', {'form': form, 'title': 'Add Employee'})


@login_required
def employee_edit_page(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/edit.html', {'form': form, 'title': 'Edit Employee'})


@login_required
def employee_delete_page(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/delete.html', {'employee': employee})
