from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializers(serializers.Serializer):
    class meta:
        model = User
        fields = [
            'user_id', 'username', 'email', 
            'first_name', 'last_name', 'phone_number', 
            'role', 'created_at'
            ]

class MessageSerializers(serializers.Serializer):
    sender = UserSerializers(read_only=True)

    class meta:
        model = Message
        fields = [
            'message_id', 'sender', 'message_body', 
            'conversation', 'sent_at'
        ]

class ConversationSerializers(serializers.Serializer):
    messages = MessageSerializers(many=True, read_only=True)
    participants = UserSerializers(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at', 'messages']
