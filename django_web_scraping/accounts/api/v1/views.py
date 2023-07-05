from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializer import RegisterUserSerializer, ChangePassWordSerializer


class RegisterUser(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer


class ChangePasswords(UpdateAPIView):
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePassWordSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if self.object.check_password(serializer.data.get("old_pass")) is False:
            return Response({"Error": "wrong old password"}, status=status.HTTP_401_UNAUTHORIZED)
        self.object.set_password(serializer.data.get("new_pass"))
        self.object.save()
        return Response({"Status ": "changed"}, status=status.HTTP_202_ACCEPTED)

