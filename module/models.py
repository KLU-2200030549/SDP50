from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    comments = models.TextField()
    class Meta:
        db_table="FeedBack"

class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    phonenumber=models.PositiveBigIntegerField()
    password=models.CharField(max_length=100)
    class Meta:
        db_table="register"

class FeedbackList(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=20)
    comments = models.TextField()
    class Meta:
        db_table="FeedBackList"