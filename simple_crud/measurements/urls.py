from rest_framework.routers import DefaultRouter

from measurements.views import ProjectViewSet, MeasurementViewSet

router = DefaultRouter()
router.register('project', ProjectViewSet)
router.register('measurements', MeasurementViewSet)

urlpatterns = router.urls
