from rest_framework import permissions

from hr.models import Employee


class ProjectAddPermission(permissions.BasePermission):
    message = "Project add permission deny"

    edit_methods = ("PUT", "PATCH", "POST")
    safe_methods = ("GET", "HEAD", "OPTIONS")
    allowed_employee_categories = ("Engineering",)

    def get_user_perm(self, request, view, obj):
        try:
            emp = Employee.objects.get(employeeUserName=request.user)

            if emp.IsSuperVisor and emp.employeeCategory.__str__() in self.allowed_employee_categories:
                return True
            if request.method in self.safe_methods and emp.employeeCategory in self.allowed_employee_categories:
                return True
            print("reach false ")
            return False
        except Employee.DoesNotExist:
            print("Can't get emp " )
            return False

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if True:
                return self.get_user_perm(request, view, "")

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if obj.author == request.user:
            return True
        if True:
            return self.get_user_perm(request, view, obj)