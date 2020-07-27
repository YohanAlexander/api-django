from django.urls import path
from django.urls import include

from api.views import ClienteViewSet
from api.views import EnderecoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet)
router.register(r'endereco', EnderecoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]

