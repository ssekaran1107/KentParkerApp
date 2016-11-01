from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Tag(models.Model):
	name=models.CharField(max_length=10)
	def __str__(self):
		return self.name

class MyUser(AbstractUser):
	picture=models.ImageField(upload_to="profile_photos",null=True,blank=True)
	email_verify=models.BooleanField(default=False)
	tags=models.ManyToManyField(Tag,null=True,blank=True)
	location=models.CharField(max_length=50)
	website=models.URLField(max_length=200)
	contacts=models.ForeignKey('self',null=True,blank=True,related_name='contacts_f')
	user_type=models.IntegerField()
	# newsmaker 1
	# journalist 2
	# mediaoutlet 3
	category=models.CharField(max_length=50)
	bio=models.CharField(max_length=420, blank=True, default="")
	organization=models.ForeignKey('self',null=True,blank=True,related_name='organization_f')


	def __str__(self):
		return self.username


class Pitch(models.Model):
	title=models.CharField(max_length=30)
	content=models.TextField()
	author=models.ForeignKey(MyUser,related_name='author_pr') # newsmaker
	tags=models.ForeignKey(Tag,null=True,blank=True)
	pub_time=models.DateTimeField(auto_now_add=True)
	last_modified_time=models.DateTimeField(auto_now=True)
	attachment=models.URLField(max_length=200)
	special=models.CharField(max_length=1)
	location=models.CharField(max_length=50)
	bookmarked=models.ForeignKey(MyUser,related_name='bookmarked_pr')

	class Meta:
		ordering=['-pub_time']

class Embargo(Pitch):
	embargo_date=models.DateTimeField()
	selected_journalists=models.ForeignKey(MyUser,null=True,blank=True) # Journalist

class Scoop(Pitch):
	selected_journalist=models.ForeignKey(MyUser) # Journalist
	status=models.BooleanField()	


class Article(models.Model):
	title=models.CharField(max_length=30)
	content=models.TextField()
	author=models.ForeignKey(MyUser,related_name='author_ar') #Journalist
	newsmaker=models.ManyToManyField(MyUser,related_name='newsmaker_am')
	tags=models.ForeignKey(Tag)
	pub_time=models.DateTimeField(auto_now_add=True)
	last_modified_time=models.DateTimeField(auto_now=True)
	related_pitch=models.ForeignKey(Pitch)
	attachment=models.URLField(max_length=200)

	class Meta:
		ordering=['-pub_time']

class Message(models.Model):
	sender=models.ForeignKey(MyUser,related_name='sender')
	receiver=models.ForeignKey(MyUser,related_name='receiver')
	content=models.TextField()
	send_time=models.DateTimeField(auto_now_add=True)
	attachment=models.URLField(max_length=200)

	def __str__(self):
		return self.content

	# sort the message based on send time in reverse order
	class Meta:
		ordering=['-send_time']

# we maintain a relation table which keeps tracking of the folower/followee relationship
# between any two types of users
# class Relation(models.Model):
# 	follower=models.ForeignKey(BaseUser,related_name='follower')
# 	followee=models.ForeignKey(BaseUser,related_name='followee')

# 	def __str__(self):
# 		return self.follower+" -> "+self.followee