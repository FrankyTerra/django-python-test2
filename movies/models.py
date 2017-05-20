from datetime import datetime
from django.db import models
from django.utils import timezone
from treebeard.mp_tree import MP_Node

from django.contrib.postgres.fields import ArrayField

class Genre(models.Model):
	genre_name = models.CharField(max_length=100)

	def __str__(self):
		return self.genre_name

class Country(models.Model):
	country_name = models.CharField(max_length=100)

	def __str__(self):
		return self.country_name

class Film(models.Model):
	film_name = models.CharField(max_length=200)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
	year_of_issue = models.DateField()
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	producer = models.CharField(max_length=200)
	pub_date = models.DateField('date published', default=datetime.now)
	cast = models.TextField()

	def __str__(self):
		return self.film_name

class Comment(MP_Node):
	film = models.ForeignKey(Film)
	author = models.CharField(max_length=100)
	text = models.TextField()
	pub_date = models.DateTimeField('date published', default=datetime.now)

	node_order_by = ['author']

	def __str__(self):
		return self.author

class Comment2(models.Model):
	path = ArrayField(models.IntegerField())
	film_id = models.ForeignKey(Film)
	author = models.CharField(max_length=100)
	content = models.TextField('Комментарий')
	pub_date = models.DateTimeField('Дата комментария', default=datetime.now)

	def __str__(self):
		return self.content[0:200]

	def get_offset(self):
		level = len(self.path) - 1
		if level > 5:
			level = 5
		return level

	def get_col(self):
		level = len(self.path) - 1
		if level > 5:
			level = 5
		return 12 - level