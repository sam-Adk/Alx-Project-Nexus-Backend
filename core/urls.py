# core/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from products.views import ProductViewSet, CategoryViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="ProDev E-Commerce API",
      default_version='v1',
      description="Fully featured e-commerce backend",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('users.urls')),
    
    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
