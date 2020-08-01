# the file is for permissions for the authenticated user to add, update or delete
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # The request is authenticated as a user, or is a read-only request.
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are only allowed to the author of a post
        return obj.author == request.user
