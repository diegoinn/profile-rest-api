"""Projects Django"""
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    """Project model"""
    name_project = models.CharField(max_length=255)
    use = models.CharField(max_length=255)
    builded_surface = models.IntegerField()
    living_area = models.IntegerField()
    tier = models.IntegerField()
    useful_life = models.IntegerField()

    def __str__(self):
        """Return string representation of project"""
        return self.name_project

class Material(models.Model):
    """Construction system model"""
    name_material = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name_material"""
        return self.name_material

class Section(models.Model):
    """Section model"""
    name_section = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name_section"""
        return self.name_section

class Origin(models.Model):
    """Origin model"""
    name_origin = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name_origin"""
        return self.name_origin

class ConstructionSystem(models.Model):
    """Construction system model"""
    name_construction_system = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name_construction_system"""
        return self.name_construction_system

class Unit(models.Model):
    """Construction unit model"""
    name_unit = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name unit"""
        return self.name_unit

class Standard(models.Model):
    """Construction standard model"""
    name_standard = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name standard"""
        return self.name_standard

class PotentialType(models.Model):
    """Construction potential type model"""
    name_potential_type = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name potential type"""
        return self.name_potential_type

class MaterialSchemeProject(models.Model):
    """MaterialSchemeProject model"""
    material_id = models.ForeignKey(Material, on_delete=models.DO_NOTHING)
    project_id = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    origin_id = models.ForeignKey(Origin, on_delete=models.DO_NOTHING)
    construction_system_id = models.ForeignKey(ConstructionSystem, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    unit_id = models.ForeignKey(Unit, on_delete=models.DO_NOTHING)
    provider_distance = models.IntegerField()

    def __str__(self):
        """Return string representation of material"""
        return self.material_id

class MaterialSchemeData(models.Model):
    """MaterialSchemeData model"""
    material_id = models.ForeignKey(Material, on_delete=models.DO_NOTHING)
    standard_id = models.ForeignKey(Standard, on_delete=models.DO_NOTHING)
    potential_type_id = models.ForeignKey(PotentialType, on_delete=models.DO_NOTHING)
    unit_id = models.ForeignKey(Unit, on_delete=models.DO_NOTHING)
    value = models.IntegerField()

    def __str__(self):
        """Return string representation of material"""
        return self.value
