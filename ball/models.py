from django.db import models


class Viloyat(models.Model):
     title = models.CharField(max_length=50)
     foiz = models.IntegerField(default=0)


class Tuman(models.Model):
     title = models.CharField(max_length=50)
     viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE, related_name='tuman')
     


class Maktab(models.Model):
     title = models.CharField(max_length=50)
     tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE, related_name='maktab')


class Oquvchi(models.Model):
     name = models.CharField(max_length=50)
     maktab = models.ForeignKey(Maktab, on_delete=models.CASCADE, related_name='oquvchi')



class Result(models.Model):
     student = models.ForeignKey(
          Oquvchi, on_delete=models.CASCADE, related_name="results"
    )
     correct_answers = models.IntegerField()
     total_answers = models.IntegerField()
     percentage = models.FloatField()
     created_at = models.DateTimeField(auto_now_add=True)


     def foiz(self):
          total = (self.jami / self.togri)*100
          return total
