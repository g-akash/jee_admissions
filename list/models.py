from django.db import models

# Create your models here.

class Programme(models.Model):
	inst = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	code = models.CharField(max_length=100)
	geo = models.IntegerField(default=0)
	gec = models.IntegerField(default=0)
	obco =models.IntegerField(default=0)
	obcc = models.IntegerField(default=0)
	sco = models.IntegerField(default=0)
	scc = models.IntegerField(default=0)
	sto = models.IntegerField(default=0)
	stc = models.IntegerField(default=0)
	geopd = models.IntegerField(default=0)
	gecpd = models.IntegerField(default=0)
	obcopd =models.IntegerField(default=0)
	obccpd = models.IntegerField(default=0)
	scopd = models.IntegerField(default=0)
	sccpd = models.IntegerField(default=0)
	stopd = models.IntegerField(default=0)
	stcpd = models.IntegerField(default=0)
	def __str__(self):
		return self.code

class inst(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name
