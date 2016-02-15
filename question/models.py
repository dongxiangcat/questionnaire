from django.db import models
from theme.models import Theme
from django.utils import timezone
# Create your models here.

class Question(models.Model):

    title       = models.CharField(max_length=250,null=False,default='')
    description = models.CharField(max_length=250,null=False,default='')
    theme       = models.ForeignKey(Theme)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)

    def __unicode__(self):
    	return self.title
    
    class Meta:
        get_latest_by  = ('id')
        ordering       = ('id','create_at')


class Answer(models.Model):

	content		= models.CharField(max_length=250,null=False,default='')
	sign		= models.CharField(max_length=100,null=False,default='')
	select_num	= models.IntegerField()
	question    = models.ForeignKey(Question)
	create_at	= models.DateTimeField(auto_now_add=True)
	update_at	= models.DateTimeField(auto_now=True)

	class Meta:
		ordering		= ('sign',)
