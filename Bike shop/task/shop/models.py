from django.db import models

# write your models here



class Frame(models.Model):
    color = models.CharField(max_length=64)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color


class Seat(models.Model):
    color = models.CharField(max_length=64)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color


class Tire(models.Model):
    type = models.CharField(max_length=64)
    quantity = models.IntegerField()

    def __str__(self):
        return self.type


class Basket(models.Model):
    quantity = models.IntegerField()


class Bike(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    has_basket = models.BooleanField()

    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    status = models.CharField(max_length=1, choices=(('P', "Pending"),('R', "Ready")))