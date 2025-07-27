from rest_framework import routers 
from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet, UserViewSet

router =routers.DefaultRouter()

router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
