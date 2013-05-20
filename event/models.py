from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	email = models.EmailField('Email Address')
	telefon = models.CharField(max_length=200)
	avatar = models.ImageField('Avatar', upload_to='profileimg/', blank=True, null=True)

class Event(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	start_date = models.DateTimeField()
	finish_date = models.DateTimeField()
	publication_date = models.DateTimeField()
	#duration = models.FloatField()
	price = models.IntegerField()
	spot = models.ForeignKey('Spot')
	type_event = models.ForeignKey('EventType')	

	def __unicode__(self):
		return self.title + unicode(self.start_date)

# Defines what kind of event is: Concert, Cinema, Meeting, etc
class EventType(models.Model):
	title = models.CharField(max_length=200)
	sub_type = models.ForeignKey('SubEventType')

	def __unicode__(self):
		return self.title

# Defines the subevent type, Concert: rock, pop. Cinema: Thriller, Terror
class SubEventType(models.Model):
	title = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title

# Where the event is located: London bar: kensinton street, 29, tlf 699 555 555
class Spot(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	telefon = models.CharField(max_length=10)
	location_map = models.CharField(max_length=1000)
	city = models.ForeignKey('City')

	def __unicode__(self):
		return self.name

# City where the event is located
class City(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name
