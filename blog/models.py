from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateField()
	image = models.ImageField(upload_to='images/')
	body = models.TextField()

	def __str__(self):
		return self.title

	def summary(self):
		if len(self.body) < 100:
			return self.body
		return self.body[:100] + '...'
