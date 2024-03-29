from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenVerifyView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="BotEcommerce New",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="xolmomin@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
                  path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('admin/', admin.site.urls),
                  path('api/v1/', include('apps.urls')),
                  path('api-auth/', include('rest_framework.urls')),
                  path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
                  path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
