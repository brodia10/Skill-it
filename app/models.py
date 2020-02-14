from django.db import models

class Skillset(models.Model):
	javascript = 'JavaScript'
	python = 'Python'
	java = 'Java'
	c_cpp = 'C and CPP'
	php = 'PHP'
	swift = 'Swift'
	c_sharp = 'C#'
	ruby = 'Ruby'
	objective_c = 'Objective C'
	sql = 'SQL'

	language_choices = (
		(javascript, 'JavaScript'),
		(python, 'Python'),
		(java, 'Java'),
		(c_cpp, 'C and/or CPP'),
		(php, 'PHP'),
		(swift, 'Swift'),
		(c_sharp, 'C#'),
		(ruby, 'Ruby'),
		(objective_c, 'Objective C'),
		(sql, 'SQL'),
	)

	company_name = models.CharField(max_length=255)
	company_size = models.IntegerField()
	location = models.CharField(max_length=255)
	remote_work = models.BooleanField()
	language_requirement = models.CharField(max_length=20, choices=language_choices, default=javascript)