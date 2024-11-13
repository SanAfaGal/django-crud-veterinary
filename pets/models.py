from django.db import models
from django.db.models import Q


class Customer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    identification = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True, default=None)
    phone_number = models.CharField(max_length=15, unique=True)

    class Meta:
        db_table = "tbl_customers"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique_customer_name')
        ]
        indexes = [
            models.Index(fields=['identification']),
        ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    id_pet = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_pets"
        verbose_name = "Pet"
        verbose_name_plural = "Pets"
        constraints = [
            models.CheckConstraint(check=Q(age__gt=0), name='age_gt_zero'),
            models.CheckConstraint(check=Q(weight__gt=0), name='weight_gt_zero'),
        ]
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f'{self.name} - {self.owner}'
