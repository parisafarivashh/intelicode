from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.serializers import TranslateSerializer


class TranslateView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = TranslateSerializer

    def post(self, request, *args, **kwargs): # added message model
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

