from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):

   def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for everyone (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True
        
        # Write permissions are only allowed for the owner of the object
        return obj.user == request.user 


