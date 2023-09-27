from django.db import models

class MathTest(models.Model):
    question = models.CharField(max_length=200)
    answer = models.IntegerField()

    def __str__(self):
        return self.question
