# set up premissions
from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        #  use safe method
        # check if user is the user who logged in
        if request.method in permissions.SAFE_METHODS:
            return True
            # check if user autenicated
        return obj.id == request.user.id

# add permissions for userProfile feed
class PostOwnStatus(permissions.BasePermission):
    """Allow users to update their own status."""

    def has_object_permission(self,request,view,obj):
        """Checks the user is trying to update their own status."""
        # check if user can update
        if request.method in permissions.SAFE_METHODS:
            return True
        # here we use model field to set specification on permission
        # if it is true that will let update
        return obj.user_profile.id == request.user.id