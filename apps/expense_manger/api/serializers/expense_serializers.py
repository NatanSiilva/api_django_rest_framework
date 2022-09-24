from rest_framework import serializers

from apps.expense_manger.models import *

class SupplierRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        # exclude = ('state','created_date','modified_date','deleted_date')
        fields = '__all__'

    def save(self):
        new_supplier = Supplier.objects.create(**self.validated_data)
        return new_supplier.to_dict()

class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        # exclude = ('state','created_date','modified_date','deleted_date')
        fields = '__all__'
    
        