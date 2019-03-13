from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')

urlpatterns = router.urls # this will give us the routers that were registered to this endpoint instead of typing them in leadmanager/urls.py