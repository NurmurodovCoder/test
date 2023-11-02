from django.db import models


# class Base(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(author="Roald Dahl")


class Category(models.Model):
     title = models.CharField(max_length=100)

     create_at = models.DateTimeField(auto_now_add=True)
     update_At = models.DateTimeField(auto_now=True)



     def __str__(self):
          return self.title
     

class Ads(models.Model):
     title = models.CharField(max_length=50)
     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ads')
     price = models.IntegerField()
     views = models.IntegerField()

     create_at = models.DateTimeField(auto_now_add=True)
     update_At = models.DateTimeField(auto_now=True)


     def __str__(self):
          return self.title
     