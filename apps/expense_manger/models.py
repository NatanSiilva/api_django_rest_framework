from django.db import models

from apps.base.models import BaseModel
from apps.products.models import Product

class Supplier(BaseModel):
    ruc = models.CharField(unique=True, max_length=11)
    business_name = models.CharField('Business name', unique=True, max_length=150, null=False, blank=False)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.business_name

    def to_dict(self):
        return {
            'id': self.id,
            'ruc': self.ruc,
            'business_name': self.business_name,
            'address': self.address,
            'phone': self.phone,
            'email': self.email
        }

class PaymentType(BaseModel):
    name = models.CharField('Name', unique=True, max_length=50, null=False, blank=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'Payment type'
        verbose_name_plural = 'Payment types'

    def __str__(self):
        return self.name


class Voucher(BaseModel):
    name = models.CharField('Name', unique=True, max_length=50, null=False, blank=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'Voucher'
        verbose_name_plural = 'Vouchers'

    def __str__(self):
        return self.name


class ExpenseCategory(BaseModel):
    name = models.CharField('Name', unique=True, max_length=50, null=False, blank=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'Expense category'
        verbose_name_plural = 'Expense categories'

    def __str__(self):
        return self.name

class Expense(BaseModel):
    date = models.DateField('Date', auto_now=False, auto_now_add=False)    
    quantity = models.DecimalField('Quantity', max_digits=10, decimal_places=2)
    unit_price = models.DecimalField('Unity Price', max_digits=10, decimal_places=2, default=0)
    voucher_number = models.CharField('Voucher Number', max_length=50)
    total = models.DecimalField('Total', max_digits=10, decimal_places=2, default=0)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'

    def __str__(self):
        return self.voucher_number

class Merma(BaseModel):
    date = models.DateField('Date', auto_now=False, auto_now_add=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField('Quantity', max_digits=7, decimal_places=2)
    lost_money = models.DecimalField('Lost Money', max_digits=7, decimal_places=2)

    class Meta:
        ordering = ['id']
        verbose_name = 'Merma'
        verbose_name_plural = 'Mermas'


    def __str__(self):
        return "Merma de {0}".format(self.product.__str__())