from django.db import models
'''
Migrations workflow 

IMportant : Make sure your app is in INSTALLED_APS
Step 1: CHnage model code
Step 2: Generate migration script
python manage.py makemigrations
Step 3: Run migrations
python manage.py migrate
Id proivded automatically by django

save() does SQL insert or update
'''

class Product(models.Model):
    name = models.CharField(max_length=100)
    stock_count = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="")

