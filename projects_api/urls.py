from django.urls import path, include

from rest_framework.routers import DefaultRouter

from projects_api import views

router = DefaultRouter()
router.register('projects', views.ProjectsViewSet)
router.register('materials', views.MaterialsViewSet)
router.register('sections', views.SectionsViewSet)
router.register('origins', views.OriginsViewSet)
router.register('construction-system', views.ConstructionSystemsViewSet)
router.register('material-scheme-project', views.MaterialSchemeProjectViewSet)
router.register('units', views.UnitsViewSet)
router.register('standards', views.StandardsViewSet)
router.register('potential-types', views.PotentialTypesViewSet)
router.register('material-scheme-data', views.MaterialSchemeDataViewSet)

urlpatterns = [
    path('', include(router.urls))
]
