from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from projects_api import models
from projects_api import serializers
from profiles_api import permissions

class ProjectsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.ProjetcsSerializer
    queryset = models.Project.objects.all()
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (permissions.UpdateOwnProjects,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_project',)

class SectionsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating sections"""
    serializer_class = serializers.SectionsSerializer
    queryset = models.Section.objects.all()
    #authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_section', )

class OriginsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating origins"""
    serializer_class = serializers.OriginsSerializer
    queryset = models.Origin.objects.all()
    #authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_origin', )

class ConstructionSystemsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating construction systems"""
    serializer_class = serializers.ConstructionSystemsSerializer
    queryset = models.ConstructionSystem.objects.all()
    #authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_construction_system', )

class MaterialSchemeProjectViewSet(viewsets.ModelViewSet):
    """Handle creating and updating materials"""
    serializer_class = serializers.MaterialSchemeProjectSerializer
    queryset = models.MaterialSchemeProject.objects.all()
    #authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name_material', )
