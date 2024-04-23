from rest_framework import serializers


class TranslateSerializer(serializers.ModelSerializer):
    text = serializers.CharField()
    translate_to = serializers.ChoiceField(choices=['en', 'fa'])

