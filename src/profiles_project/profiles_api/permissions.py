# set up premissions
from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""
    def has_object_premission(self,request,view,obj):
        """Check user is trying to edit their own profile"""
        #  use safe method
        # check if user is the user who logged in
        if request.method in permissions.SAFE_METHODS:
            return True

        # checking if user authenificated
        return obj.id == request.user.id

