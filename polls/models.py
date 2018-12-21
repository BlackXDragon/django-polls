from django.db import models

import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	qText = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def __str__(self):
		return self.qText
	
	def recent(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	recent.admin_order_field = 'pub_date'
	recent.boolean = True
	recent.short_description = "Recent?"

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	cText = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	
	def __str__(self):
		return self.cText