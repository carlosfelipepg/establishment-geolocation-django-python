from django.contrib.auth import authenticate

from rest_framework import viewsets, exceptions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from user.serializers import UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (AllowAny,)

    # http_method_names = ['get']

    def create(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']

        user_data = {
            'password': password,
            'username': username
        }

        serializer = self.serializer_class(data=user_data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(username=username, password=password, is_active=True)

        token = Token.objects.get_or_create(user=user)[0]

        return Response({
            'detail': 'Cadastro conclúido com sucesso',
            'token': token.key
        }, status=status.HTTP_200_OK)

    @action(methods=["post"], detail=False)
    def login(self, request):
        password = request.data.get('password', None)
        username = request.data.get('username', None)

        if not password:
            raise exceptions.AuthenticationFailed('Senha inválida')

        user = authenticate(
            password=password,
            username=username
        )
        if not user:
            raise exceptions.AuthenticationFailed('Usuário não encontrado')

        return Response({
            'detail': 'success',
            'token': user.auth_token.key,
            'username': user.username
        }, status=status.HTTP_200_OK)
