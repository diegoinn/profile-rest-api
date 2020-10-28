"""Projects Django"""
from django.db import models
from django.contrib.auth.models import User

class Section(models.Model):
    """Section model"""
    name_section = models.CharField(max_length=255)

    def __str__(self):
        """Return string representation of name_section"""
        return self.name_section

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


class MaterialSchemeProject(models.Model):
    """MaterialSchemeProject model"""
    name_material = models.CharField(max_length=255)
    project_id = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    origin_id = models.ForeignKey(Origin, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    unit = models.IntegerField()
    construction_system_id = models.ForeignKey(ConstructionSystem, on_delete=models.DO_NOTHING)

    def __str__(self):
        """Return string representation of material"""
        return self.name_material
