from rest_framework import permissions


class IsAuthorOrReadOnLy(permissions.BasePermission):
    message = 'Изменение чужого контента запрещено!'

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class ReadOnly(permissions.BasePermission):
    message = 'Без аутентификации доступно только чтение!'

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
