from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    """
    Permite lectura a usuarios autenticados.
    Escritura solo a usuarios staff y NADIE MASSSSSSSSSS.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated

        return request.user and request.user.is_staff
