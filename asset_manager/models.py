from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=60)
    #location = models.FilePathField()
    date = models.DateTimeField(auto_now_add=True)


class Asset(models.Model):
    name = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=40)
    project = models.ForeignKey(Project, related_name='project')


class SubAsset():

    departments = (
        (0, '----'),
        (1, 'Lighting'),
        (2, 'Rigging'),
        (3, 'Modeling'),
        (4, 'Art/Design'),
        (5, 'Animation'),
        (6, 'R&D'),
        (7, 'tests'),
    )

    name = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=40)
    asset = models.ForeignKey(Asset, related_name='Asset')
    location = models.FilePathField()
    department = models.CharField(departments)
