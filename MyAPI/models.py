from django.db import models


class Directions(models.Model):
    name = models.CharField(max_length=355)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    numb = models.IntegerField()

    def __str__(self):
        return self.name


class Doctors(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug', default=0)
    directions = models.ManyToManyField(Directions)
    description = models.TextField(max_length=255, default='')
    birt_date = models.DateField(verbose_name='Birth date', null=True)
    work_experience = models.TextField(max_length=255, default='')
    numb = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
