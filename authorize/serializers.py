from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token


class DRFTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user) -> Token:
        token = super().get_token(user)
        token['email'] = user.email
        return token

