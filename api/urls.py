from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

from api.views.customer_view import CustomerView
from rest_framework.schemas import get_schema_view

router = routers.DefaultRouter()
router.register(r"customer", CustomerView, basename="customer")


urlpatterns = [
    path("auth/login/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh",),
    path("", include(router.urls)),
    path(
        "openapi/",
        get_schema_view(
            title="Challenge Luiza Labs",
            description="API for test purposes",
            version="1.0.0",
            public=True,
            permission_classes=[AllowAny],
        ),
        name="openapi-schema",
    ),
    path(
        "docs/",
        TemplateView.as_view(
            template_name="documentation.html", extra_context={"schema_url": "openapi-schema"}
        ),
        name="swagger-ui",
    ),
]

