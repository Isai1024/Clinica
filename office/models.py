from django.db import models

# Create your models here.

class Office(models.Model):
    id = models.AutoField(primary_key=True)
    
    office_name = models.CharField(max_length=255)
    is_used = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'offices'
        ordering = ['id']