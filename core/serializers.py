from rest_framework import serializers

from .models import Message


class TranslateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['body', 'translate_to', 'sender_id']
        extra_kwargs = {'sender_id': {'required': False}}


