from django.contrib import admin
from .models import Store


# Register your models here.
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'CustomerCode',
        'CustomerName',
        'SiteCode',
        'InvoiceNo',
        'ItemNo',
        'SalesOrderNo',
        'CustomerPONo',
        'InvoiceDate',
        'Article',
        'EAN',
        'Quantity',
        'UOM',
        'MRPPerUnit',
        'GrossAmount',
        'BasicValue',
        'TaxableValue',
        'TotalInvAmt',
        'EmployeeName',
        'EmployeeCode', ]
