from django.db import models

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length = 200)
    qty = models.IntegerField()

    def __str__(self):
        return self.name
    
class StockIn(models.Model):
    item = models.ForeignKey(Items,blank=True,default=True,on_delete=models.CASCADE)
    qty = models.IntegerField()
    purchased_from = models.CharField(max_length = 50)
    bill_no = models.CharField(max_length = 10)
    bill_amount = models.FloatField()
    purchased_by = models.CharField(max_length = 50)

    def __str__(self):
        return self.item.name
    
class StockOut(models.Model):
    item = models.ForeignKey(Items,blank=True,default=True,on_delete=models.CASCADE)
    qty = models.IntegerField()
    out_by = models.CharField(max_length = 50,default= " ")

    def __str__(self):
        return self.item.name

