from django.db import models

class Bag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

#class Addon(models.Model):
#    name = models.CharField(max_length=30)
#    short_title = models.CharField(max_length=15)
#
#    def __str__(self):
#        return self.name

class Label(models.Model):
    sku = models.CharField(max_length=100)
    header = models.CharField(max_length=100)
    fnsku = models.CharField(max_length=10)
    bag = models.ForeignKey(Bag, on_delete=models.PROTECT, blank=True, null=True)
#    addon = models.ForeignKey(Addon, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.sku
