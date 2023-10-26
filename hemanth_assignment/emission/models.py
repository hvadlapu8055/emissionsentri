from django.db import models

# Create your models here.
class Emissions(models.Model):
    # Id field is automatically created as the primary key
    date_created = models.DateField()
    accounting_period = models.CharField(max_length=255)
    scope_1 = models.IntegerField(blank=True, null=True)
    scope_2 = models.IntegerField(blank=True, null=True)
    scope_3 = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Emissions Entry {self.id} - {self.accounting_period}"
