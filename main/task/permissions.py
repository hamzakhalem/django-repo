from rest_framework import permissions

class IsTaskListOwnerOrGetAndPostOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return request.user.profile == obj.created_by

        return False

class IsTaskOwnerOrGetAndPostOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return request.user.house != None
        return False
    
    def has_object_permission(self, request, view, obj):

        if not request.user.is_anonymous:
            return request.user.profile == obj.task_list.house

        return False

class IsAttachmentOwnerOrGetAndPostOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return request.user.house != None
        return False
    
    def has_object_permission(self, request, view, obj):

        if not request.user.is_anonymous:
            return request.user.profile == obj.task.task_list.house

        return False
