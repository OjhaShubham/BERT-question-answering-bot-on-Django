from pyexpat import model
from django.db import models

# Create your models here.

class Question(models.Model):
    question=models.TextField(null=False)
    wiki_terms=models.CharField(max_length=255,null=False)
    wiki_text=models.TextField(null=False)
    answer=models.CharField(max_length=200)
    prediction_score=models.FloatField(default=0)
