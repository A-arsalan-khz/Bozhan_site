# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class UserPublicinformation(models.Model):
    type_approval_number = models.TextField(blank=True, null=True)
    typee = models.TextField(blank=True, null=True)
    brand_name = models.CharField(max_length=11, blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    model = models.TextField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    production_date = models.CharField(max_length=10, blank=True, null=True)
    delivery_date = models.CharField(max_length=10, blank=True, null=True)
    vin = models.CharField(max_length=17, blank=True, null=True)
    essential_accessories = models.IntegerField(blank=True, null=True)
    additional_features = models.IntegerField(blank=True, null=True)
    net_power_of_motive_forces = models.CharField(max_length=4, blank=True, null=True)
    torque = models.CharField(max_length=4, blank=True, null=True)
    maximum_speed = models.CharField(max_length=4, blank=True, null=True)
    fuel_consumption = models.CharField(max_length=4, blank=True, null=True)
    energy_rating = models.CharField(max_length=4, blank=True, null=True)
    battery_type = models.CharField(max_length=4, blank=True, null=True)
    battery_capacity = models.CharField(max_length=4, blank=True, null=True)
    navigation_per_charge = models.CharField(max_length=12, blank=True, null=True)
    pure_mass = models.CharField(max_length=6, blank=True, null=True)
    maximum_permissible_technical_mass = models.CharField(max_length=6, blank=True, null=True)
    pollution_standard_level = models.CharField(max_length=4, blank=True, null=True)
    static_sound_level = models.CharField(max_length=4, blank=True, null=True)
    guarantee_period = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_publicinformation'
