from rest_framework import permissions


class updateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHOD:
            return True

        return obj_user_profile.id == request.user.id
