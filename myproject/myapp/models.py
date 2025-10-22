# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Property(models.Model):
    id = models.BigIntegerField(primary_key=True)
    type = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    use_start_date = models.TextField(db_column='useStartDate', blank=True, null=True)  # Field name made lowercase.
    deterioration = models.TextField(blank=True, null=True)
    wall_materials = models.TextField(db_column='wallMaterials', blank=True, null=True)  # Field name made lowercase.
    plottage = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    contacts_name = models.TextField(db_column='contactsName', blank=True, null=True)  # Field name made lowercase.
    contacts_phone = models.TextField(db_column='contactsPhone', blank=True, null=True)  # Field name made lowercase.
    contacts_email = models.TextField(db_column='contactsEmail', blank=True, null=True)  # Field name made lowercase.
    price = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


    class Meta:
        managed = False
        db_table = 'abandoned_objects'
