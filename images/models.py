from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length = 200)
    image_path = models.CharField(max_length = 300)
    stars = models.IntegerField(default = 0)
    pub_date = models.DateTimeField('data published')
    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def age_days(self):
        day_born = datetime.datetime.strptime("2016-08-29", "%Y-%m-%d")
        pub_date = datetime.datetime.strptime(str(self.pub_date)[:10], "%Y-%m-%d")
        # pub_date = datetime.datetime.strptime("2020-01-29", "%Y-%m-%d")
        return str(abs((pub_date-day_born).days / 365))[:4]
    def __str__(self):
        return self.image_name

class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete = models.CASCADE)
    comment_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.comment_text

