from djongo import models

# Create your models here.
class product(models.Model):
    product_name=models.CharField(max_length=250,null=False)
    product_code=models.IntegerField(default=0)
    original_price=models.IntegerField(default=0)
    selling_price=models.IntegerField(default=0)
    product_qty=models.IntegerField(default=0)


@property
def mongo_id(self):
    return str(self._id)

def _str_(self):
    return self.name

