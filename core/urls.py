from django.urls import path

from .views import TranslateView, ChatView


urlpatterns = [
    path('translate', TranslateView.as_view(), name='translate'),
    path('chat', ChatView.as_view(), name='chat'),
]
