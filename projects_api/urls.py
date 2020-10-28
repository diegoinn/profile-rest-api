from django.urls import path, include

from rest_framework.routers import DefaultRouter

from projects_api import views

router = DefaultRouter()
router.register('projects', views.ProjectsViewSet)
router.register('sections', views.SectionsViewSet)
router.register('origin', views.OriginsViewSet)
router.register('construction-system', views.ConstructionSystemsViewSet)
router.register('material-scheme-project', views.MaterialSchemeProjectViewSet)

urlpatterns = [
    path('', include(router.urls))
]
