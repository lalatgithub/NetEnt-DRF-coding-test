from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow author of a Book to edit it.
    """

    def has_object_permission(self, request, view, obj):
        """
        Read permissions are allowed to public,
        so we'll always allow GET, HEAD or OPTIONS requests.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the Book.
        return obj.author == request.user
