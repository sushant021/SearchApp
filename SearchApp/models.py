from django.db import models
from django.urls import reverse

default_author = 1

class Author(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		ordering= ('-name',)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('SearchApp:view_author',args=[self.name])

class Book(models.Model):
	title  = models.CharField(max_length=200)
	slug= models.SlugField(max_length=200,unique=True)
	author = models.ForeignKey(Author, on_delete = models.PROTECT,default=default_author,related_name = 'books')
	published = models.DateField(blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('SearchApp:view_book',args=[self.title])