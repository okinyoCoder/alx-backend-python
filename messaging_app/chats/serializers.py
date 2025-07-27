from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializers(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    full_name = serializers.SerializerMethodField()
    class meta:
        model = User
        fields = [
            'user_id', 'username', 'email', 'password',
            'first_name', 'last_name', 'phone_number', 
            'role', 'created_at', 'confirm_password'
            ]
        extra_kwargs = {'password': {'write_only': True}}
    
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

        def validate(self, data):
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError("Password doesnt match.")
            return data
        
    def create(self, validated_data):
        validated_data.pop('confirm_password') 
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

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
