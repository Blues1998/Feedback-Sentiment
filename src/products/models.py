# from django.db import models

# # Create your models here.

# # Note to self: Run makemigrations and migrate every time you make a change to this file

# class Product(models.Model):
# 	title 		= 	models.CharField(blank=True,max_length=100)
# 	descript 	= 	models.TextField(blank=True, null=True)
# 	price 		= 	models.DecimalField(max_digits=10 ,decimal_places=2)
# 	feedback 	=	models.TextField(blank=True)

from django.db import models
class Review(models.Model):
   author = models.CharField(max_length=150)
   author_email = models.EmailField()
   review_title = models.CharField(max_length=300, null=True)
   review_body = models.TextField(blank=True)
   creation_date = models.DateTimeField(auto_now_add=True, blank=True)
   sentiment_score = models.DecimalField(max_digits=5, decimal_places=4)
   def is_critical(self):
       return True if self.sentiment_score < -0.2 else False
   def __str__(self):
       return self.review_title