from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin'),
    ]
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    password = models.CharField(_('password'), max_length=128)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='guest')
    created_at =models.DateField(auto_now_add=True)

    REQUIRED_FIELDS = [ 'email', 'username']
    USERNAME_FIELD = ['email']

    def __str__(self):
        return f"{self.username} ({self.role})"
    
class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    message_body = models.TextField()
    sent_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.sent_at}"
    
class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    participants_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="conversations")
    created_at = models.DateField(auto_now_add=True)