from rest_framework import routers

from .api import CustomerViewSet, PetViewSet

router = routers.DefaultRouter()
router.register('api/customers', CustomerViewSet, 'customers')
router.register('api/pets', PetViewSet, 'pets')
urlpatterns = router.urls

