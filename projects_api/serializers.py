from rest_framework import serializers

from projects_api import models

class SectionsSerializer(serializers.ModelSerializer):
    """Serializes a section object"""

    class Meta:
        model = models.Section
        fields = '__all__'

    def create(self, validated_data):
        """Used to create section"""
        section = models.Section(
            name_section=validated_data['name_section']
        )

        section.save()
        return section

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)


class ProjetcsSerializer(serializers.ModelSerializer):
    """Serializes a project object"""

    class Meta:
        model = models.Project
        fields = ('id', 'name_project', 'use', 'builded_surface', 'living_area', 'tier', 'useful_life')

    def create(self, validated_data):
        """Used to create a project."""
        project = models.Project(
            name_project=validated_data['name_project'],
            use=validated_data['use'],
            builded_surface=validated_data['builded_surface'],
            living_area=validated_data['living_area'],
            tier=validated_data['tier'],
            useful_life=validated_data['useful_life']
        )

        project.save()
        return project

    def update(self, instance, validated_data):
        """Handle updating a project"""
        return super().update(instance, validated_data)

class OriginsSerializer(serializers.ModelSerializer):
    """Serializes a origin object"""

    class Meta:
        model = models.Origin
        fields = '__all__'

    def create(self, validated_data):
        """Used to create origin"""
        origin = models.Section(
            name_origin=validated_data['name_origin']
        )

        origin.save()
        return origin

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class ConstructionSystemsSerializer(serializers.ModelSerializer):
    """Serializes a construction system object"""

    class Meta:
        model = models.ConstructionSystem
        fields = '__all__'

    def create(self, validated_data):
        """Used to create construction cystem"""
        constructionSystem = models.Section(
            name_construction_system=validated_data['name_construction_system']
        )

        constructionSystem.save()
        return constructionSystem

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class MaterialSchemeProjectSerializer(serializers.ModelSerializer):
    """Material Scheme a material object"""

    class Meta:
        model = models.MaterialSchemeProject
        fields = '__all__'

    def create(self, validated_data):
        """Used to create a material."""
        material_scheme = models.Material(
            name_material=validated_data['name_material'],
            quantity=validated_data['quantity'],
            unit=validated_data['unit'],
            project_id=validated_data['project_id'],
            origin_id=validated_data['origin_id']
        )

        material_scheme.save()
        return material_scheme

    def update(self, instance, validated_data):
        """Handle updating a material"""
        return super().update(instance, validated_data)
