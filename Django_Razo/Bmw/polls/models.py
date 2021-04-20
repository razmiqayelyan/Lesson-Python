from django.db import models

# Create your models here.
class Fabric(models.Model):
	name = models.CharField('Name Fabric',max_length=40)
	about_us = models.TextField('About as')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Fabric'

CHOICE_CLOTHING = (
	('shoes', 'SHOES'),
	('shirt', 'SHIRT'),
	('jeans', 'JEANS'),
	('polo', 'POLO'),
)

SHIRT_SIZES = (
	('S', 'Small'),
	('M', 'Medium'),
	('L', 'Large')	
)

class Clothing(models.Model):
	clothing_choice = models.CharField(max_length=8,choices=CHOICE_CLOTHING)
	shirt_size = models.CharField(max_length=1,choices=SHIRT_SIZES)
	model_clothing = models.CharField('Name model', max_length=12)
	price = models.IntegerField('Price', default=10)
	color = models.CharField('Color',max_length=20, blank=True)


	def __str__(self):
		return f'ID {self.id}, Price {self.clothing_choice}'

	class Meta:
		verbose_name = 'Clothing'
	
