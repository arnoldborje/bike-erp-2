# app_name/decorators.py
from django.http import HttpResponseForbidden
from functools import wraps

def role_required(allowed_roles):
    """
    Decorator to restrict views to specific employee roles.
    Usage:
        @role_required(['sales', 'admin'])
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Ensure the user is authenticated
            if not request.user.is_authenticated:
                return HttpResponseForbidden("You must be logged in.")

            # Ensure the user has an employee profile
            if not hasattr(request.user, 'employee_profile'):
                return HttpResponseForbidden("You are not registered as an employee.")

            # Check role
            if request.user.employee_profile.role not in allowed_roles:
                return HttpResponseForbidden("You don't have permission to access this page.")

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
