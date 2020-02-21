from django.db import models

language_choices = (
    ('JavaScript', 'JavaScript'),
    ('Python', 'Python'),
    ('Java', 'Java'),
    ('C and/or CPP', 'C and/or CPP'),
    ('PHP', 'PHP'),
    ('Swift', 'Swift'),
    ('C#', 'C#'),
    ('Ruby', 'Ruby'),
    ('Objective C', 'Objective C'),
    ('SQL', 'SQL')
)


class Skillset(models.Model):

    company_name = models.CharField(max_length=255)
    company_size = models.IntegerField()
    location = models.CharField(max_length=255)
    remote_work = models.BooleanField()
    language_requirement = models.CharField(
        max_length=20, choices=language_choices, default="Javascript")
