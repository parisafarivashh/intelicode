from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import TranslateSerializer
from .translate import translator


class TranslateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TranslateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        data = translator(
                body=request.data['body'],
                translate_to=request.data['translate_to']
        )
        return Response(data=dict(result=data), status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(sender_id=self.request.user.id)

