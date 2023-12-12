from django.db import models

class Edge(models.Model):
    start_vertex = models.IntegerField()
    end_vertex = models.IntegerField()
    weight = models.IntegerField()