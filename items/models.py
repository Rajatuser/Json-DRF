from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Store(models.Model):
    id = models.AutoField(primary_key=True)
    CustomerCode = models.CharField(max_length=20)
    CustomerName = models.CharField(max_length=100)
    SiteCode = models.CharField(max_length=10)
    InvoiceNo = models.CharField(max_length=20)
    ItemNo = models.CharField(max_length=10)
    SalesOrderNo = models.CharField(max_length=20)
    CustomerPONo = models.CharField(max_length=20)
    InvoiceDate = models.CharField(max_length=15)
    Article = models.CharField(max_length=100)
    EAN = models.CharField(max_length=20)
    Quantity = models.IntegerField()
    UOM = models.CharField(max_length=10)
    MRPPerUnit = models.DecimalField(max_digits=10, decimal_places=2)
    GrossAmount = models.DecimalField(max_digits=10, decimal_places=2)
    BasicValue = models.DecimalField(max_digits=10, decimal_places=2)
    TaxableValue = models.DecimalField(max_digits=10, decimal_places=2)
    TotalInvAmt = models.DecimalField(max_digits=10, decimal_places=2)
    EmployeeName = models.CharField(max_length=50, null=True)
    EmployeeCode = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.CustomerCode
