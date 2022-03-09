from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    photo_file = models.CharField(max_length=200)
    video_url = models.CharField(max_length=200)
    create_date = models.DateField(auto_now_add=True)
    
    
    class Meta:
        db_table = 'news'