from django.db import models

# Create your models here.

class Image(models.Model):
    class Meta:
        db_table = "images"
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=False)
    created_by  = models.ForeignKey("users.user",on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)


class Status(models.Model):
    class Meta:
        # https://english.stackexchange.com/questions/877/what-is-the-plural-form-of-status
        db_table = "statuses"
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=False,default="default")

class Auction(models.Model):
    class Meta:
        db_table = "auctions"
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=False)
    description = models.TextField(max_length=2000,null=False)
    status = models.ForeignKey("Status",on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to='uploads/')
    accepted_bid = models.ForeignKey("Bid",on_delete=models.CASCADE,null=True)
    minimal_price = models.DecimalField(max_digits=14,decimal_places=2,default=0.00)
    created_by  = models.ForeignKey("users.user",on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)


class Bid(models.Model):
    class Meta:
        db_table = "bids"
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=14,decimal_places=2)
    created_by  = models.ForeignKey("users.user",on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
