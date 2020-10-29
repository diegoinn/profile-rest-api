from rest_framework import serializers

from projects_api import models

class ProjetcsSerializer(serializers.ModelSerializer):
    """Serializes a project object"""

    class Meta:
        model = models.Project
        fields = '__all__'

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

class MaterialsSerializer(serializers.ModelSerializer):
    """Serializes a section material"""

    class Meta:
        model = models.Material
        fields = '__all__'

    def create(self, validated_data):
        """Used to create material"""
        material = models.Material(
            name_material=validated_data['name_material']
        )

        material.save()
        return material

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

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

class OriginsSerializer(serializers.ModelSerializer):
    """Serializes a origin object"""

    class Meta:
        model = models.Origin
        fields = '__all__'

    def create(self, validated_data):
        """Used to create origin"""
        origin = models.Origin(
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
        construction = models.ConstructionSystem(
            name_construction_system=validated_data['name_construction_system']
        )

        construction.save()
        return construction

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class UnitsSerializer(serializers.ModelSerializer):
    """Serializes a create unit"""

    class Meta:
        model = models.Unit
        fields = '__all__'

    def create(self, validated_data):
        """Used to create origin"""
        unit = models.Unit(
            name_unit=validated_data['name_unit']
        )

        unit.save()
        return unit

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class StandardsSerializer(serializers.ModelSerializer):
    """Serializes a create standards"""

    class Meta:
        model = models.Standard
        fields = '__all__'

    def create(self, validated_data):
        """Used to create standard"""
        standard = models.Standard(
            name_standard=validated_data['name_standard']
        )

        standard.save()
        return standard

    def update(self, instance, validated_data):
        """Handle updating a section"""
        return super().update(instance, validated_data)

class PotentialTypesSerializer(serializers.ModelSerializer):
    """Serializes a potential types"""

    class Meta:
        model = models.PotentialType
        fields = '__all__'

    def create(self, validated_data):
        """Used to create potential type"""
        potentialType = models.Standard(
            name_potential_type=validated_data['name_potential_type']
        )

        potentialType.save()
        return potentialType

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
        material_scheme = models.MaterialSchemeProject(
            material_id=validated_data['material_id'],
            project_id=validated_data['project_id'],
            origin_id=validated_data['origin_id'],
            construction_system_id=validated_data['construction_system_id'],
            quantity=validated_data['quantity'],
            unit_id=validated_data['unit_id'],
            provider_distance=validated_data['provider_distance']
        )

        material_scheme.save()
        return material_scheme

    def update(self, instance, validated_data):
        """Handle updating a material"""
        return super().update(instance, validated_data)

class MaterialSchemeDataSerializer(serializers.ModelSerializer):
    """Material Scheme a material scheme data object"""

    class Meta:
        model = models.MaterialSchemeData
        fields = '__all__'

    def create(self, validated_data):
        """Used to create a material scheme data"""
        material_scheme = models.MaterialSchemeData(
            material_id=validated_data['material_id'],
            standard_id=validated_data['standard_id'],
            potential_type_id=validated_data['potential_type_id'],
            unit_id=validated_data['unit_id'],
            value=validated_data['value']
        )

        material_scheme.save()
        return material_scheme

    def update(self, instance, validated_data):
        """Handle updating a material"""
        return super().update(instance, validated_data)
