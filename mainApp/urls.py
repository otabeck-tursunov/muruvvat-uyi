from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from .views import YangilikModelViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Muruvvat Uyi API Documentation",
        default_version="v1",
        description="Admin panel - /admin/ linkida \n"
                    "login: admin, password: 123",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="tursunovotabekkuva@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'', YangilikModelViewSet)

urlpatterns = [
    path('yangilik/', include(router.urls)),
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]
