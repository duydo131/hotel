"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import rest_framework
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter

from apps.hotel.views.hotel import HotelViewSet
from apps.hotel.views.rating import RatingViewSet
from apps.notification.views.notification import NotificationViewSet
from apps.rents.views import FeedbackViewSet
from apps.rents.views.rent import RentViewSet
from apps.rents.views.rent_detail import RentDetailViewSet
from apps.room.views.device import DeviceViewSet
from apps.room.views.room import RoomViewSet
from apps.room.views.room_category import RoomCategoryViewSet
from apps.room.views.room_device import RoomDeviceViewSet
from apps.room.views.service import ServiceViewSet
from apps.users.views import UserViewSet

swagger_info = openapi.Info(
    title="Eureka API",
    default_version="v1",
    description="""Eureka project.""",
    contact=openapi.Contact(email="hr@ftech.ai"),
    license=openapi.License(name="Private"),
)

schema_view = get_schema_view(
    info=swagger_info,
    public=True,
    authentication_classes=[
        rest_framework.authentication.SessionAuthentication
    ],
    permission_classes=[permissions.IsAdminUser],
)

api_router = SimpleRouter(trailing_slash=False)

# users
api_router.register("users", UserViewSet, basename="users")
# ---------
api_router.register("hotel", HotelViewSet, basename="hotel")
api_router.register("room", RoomViewSet, basename="room")
api_router.register("room_category", RoomCategoryViewSet, basename="room_category")
api_router.register("service", ServiceViewSet, basename="service")
api_router.register("device", DeviceViewSet, basename="device")
api_router.register("room_device", RoomDeviceViewSet, basename="room_device")
api_router.register("rent", RentViewSet, basename="rent")
api_router.register("rent_detail", RentDetailViewSet, basename="rent_detail")
api_router.register("feedback", FeedbackViewSet, basename="feedback")
api_router.register("rating", RatingViewSet, basename="rating")
api_router.register("notification", NotificationViewSet, basename="notification")

admin.autodiscover()

urlpatterns = [
    path("admin/", admin.site.urls),
    path(r"api/v1/", include(api_router.urls)),
]

urlpatterns.extend([
    path(
        r"swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
])
