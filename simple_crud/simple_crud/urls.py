from django.contrib import admin
from django.urls import path, include

# TODO: настройте роутер и подключите `ProjectViewSet` и `MeasurementViewSet`


urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include('measurements.urls')),
]
