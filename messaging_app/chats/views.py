from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsParticipantOfConversation
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all().prefetch_related('participants', 'messages')
    serializer_class = ConversationSerializer
    permission_classes = [IsParticipantOfConversation]

    def perform_create(self, serializer):
        if getattr(self, 'swagger_fake_view', False):
            return  # Prevent Swagger crash
        conversation = serializer.save()
        conversation.participants.add(self.request.user)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Conversation.objects.none()  # Prevent Swagger crash
        return self.queryset.filter(participants=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().select_related('sender', 'conversation')
    serializer_class = MessageSerializer
    permission_classes = [IsParticipantOfConversation]

    def perform_create(self, serializer):
        if getattr(self, 'swagger_fake_view', False):
            return  # Prevent Swagger crash
        serializer.save(sender=self.request.user)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Message.objects.none()  # Prevent Swagger crash
        return self.queryset.filter(conversation__participants=self.request.user)


