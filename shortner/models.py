from django.db import models

class Urls(models.Model):
    original_url = models.URLField(max_length=2048)
    short_url = models.CharField(max_length=8, unique=True)
   
    def __str__(self) -> str:
        return self.short_url
    

class Invoice(models.Model):
    customer_name = models.CharField(max_length=100)
    invoice_number = models.CharField(max_length=50)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    dynamic_url = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.customer_name


