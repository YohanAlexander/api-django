from django.urls import path
from django.urls import include

from api.views import ClienteViewSet
from api.views import EnderecoViewSet

from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register(r'cliente', ClienteViewSet)
cliente_router = routers.NestedSimpleRouter(router, r'cliente', lookup='cliente')
cliente_router.register(r'endereco', EnderecoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(cliente_router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]

