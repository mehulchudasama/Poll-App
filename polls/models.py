import datetime


from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


class Post(models.Model):

	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True,null=True)

	def __str__(self):
		return self.title

	def publish(self):
		self.published_date = timezone.now()
		self.save()



class Comment(models.Model):
	post=models.ForeignKey('polls.Post',on_delete=models.CASCADE,related_name="comments")
	user =models.ForeignKey(User,on_delete=models.CASCADE)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.text



    # ...
    # def __str__(self):
    #     return self.question_text
	
	# def was_published_recently(self):
	# 	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# class Choice(models.Model):

# 	question = models.ForeignKey(Question,on_delete=models.CASCADE)
# 	choice_text=models.CharField(max_length=200)
# 	votes=models.IntegerField(default=0)

# 	def __str__(self):
# 		return self.choice_text
# 	# ...
    