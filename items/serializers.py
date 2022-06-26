from django.contrib.auth.models import User
from .models import Store
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['CustomerCode',
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
                  'EmployeeCode']

