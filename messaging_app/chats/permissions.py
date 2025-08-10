# messaging_app/chats/permissions.py
from rest_framework import permissions
from .models import Conversation

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to only allow participants of a conversation
    to interact with its messages.
    """

    def has_permission(self, request, view):
        # Require authentication globally
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Applies to individual message or conversation
        if hasattr(obj, 'conversation'):
            # For Message object
            return request.user in obj.conversation.participants.all()
        elif hasattr(obj, 'participants'):
            # For Conversation object
            return request.user in obj.participants.all()
        return False


