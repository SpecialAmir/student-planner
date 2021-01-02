
from django.urls import path
from rest_framework import routers
from .views import *
app_name = 'plan'
router = routers.SimpleRouter()
router.register('', PlanViewSet, 'plan')
urlpatterns = router.urls
