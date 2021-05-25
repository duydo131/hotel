from django.contrib.auth import authenticate
from django.contrib.auth.models import AnonymousUser
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status, exceptions
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.filters import UserFilterSet
from apps.users.models.user import User
from apps.users.serializers import UserSerializer, UserReadOnlySerializer, LoginSerializer
from core.mixins import GetSerializerClassMixin
from core.swagger_schemas import ManualParametersAutoSchema

from apps.users.models.role import Role, RolePermissions


class UserViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer
    serializer_action_classes = {
        "list": UserReadOnlySerializer,
        "retrieve": UserReadOnlySerializer,
    }
    filterset_class = UserFilterSet

    def get_queryset(self):
        queryset = self.queryset.all()
        admin = Role.objects.get(name=RolePermissions.ADMIN)
        if not admin:
            raise Exception("Error Server")
        user = self.request.user
        if isinstance(user, AnonymousUser) or \
                not (RolePermissions.ADMIN in [role.name for role in self.request.user.roles.all()]):
            print(queryset)
            queryset = queryset.exclude(roles=admin)
            print(queryset)
        return queryset

    def perform_create(self, serializer):
        serializer.save()
        role_guest = Role.objects.get(name=RolePermissions.GUEST)
        user = dict(serializer.data)
        new_user = User.objects.get(id=user['id']);
        if not role_guest or not new_user:
            raise APIException(
                _("Cannot create user"),
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        new_user.roles.add(role_guest)
        new_user.save()

    @swagger_auto_schema(
        operation_description="Get me",
        auto_schema=ManualParametersAutoSchema,
        responses={200: UserReadOnlySerializer},
    )
    @action(
        methods=["GET"],
        detail=False,
        url_path="me",
        url_name="me",
        permission_classes=[IsAuthenticated],
        filterset_class=None,
        pagination_class=None,
    )
    def me(self, request, *args, **kwargs):
        user = request.user
        serializer = self.serializer_action_classes.get("retrieve")(
            user
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Login",
        request_body=LoginSerializer,
        auto_schema=ManualParametersAutoSchema,
        responses={200: UserReadOnlySerializer},
    )
    @action(
        methods=["POST"],
        detail=False,
        url_path="login",
        url_name="login",
        filterset_class=None,
        permission_classes=[],
        pagination_class=None,
    )
    def login(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        try:
            user = authenticate(username=username, password=password)
        except exceptions.NotFound:
            raise APIException(
                _("User or password is wrong"),
                status.HTTP_404_NOT_FOUND,
            )
        except:
            raise APIException(_("Invalid token"), status.HTTP_400_BAD_REQUEST)
        if not user:
            raise APIException(
                _("User with username {username} not found").format(username=username),
                status.HTTP_404_NOT_FOUND,
            )
        token = user.token
        data = {"token": token}
        return Response(data=data, status=status.HTTP_200_OK)
