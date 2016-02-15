from django.db import models
from django.utils import timezone
# Create your models here.


class Theme(models.Model):
    title           = models.CharField(max_length=250,null=False,default='')
    description     = models.TextField(max_length=500,null=False,default='')
    question_num    = models.IntegerField(null=False,default=0)
    create_at       = models.DateTimeField(auto_now_add=True)
    update_at       = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by   = 'id'
        ordering        = ['-id']

    def __unicode__(self):
        return self.title
    
