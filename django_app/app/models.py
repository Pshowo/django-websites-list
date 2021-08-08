from django.db import models

# Create your models here.


class Category(models.Model):
    """Store website category"""

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    count = models.IntegerField()

    def __str__(self):
        return self.name

class Website(models.Model):
    """Stored webstie details url, title, desctiption and date
    """

    url = models.URLField()
    title = models.CharField(max_length=255)
    meta_description = models.TextField()
    alexa_rank = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"url: {self.url[:12]}... rank: {self.alexa_rank}"

class WebPage(models.Model):
    """Stored webpage information"""

    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    url = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    meta_description = models.TextField()

    def __str__(self):
        return f"{self.url[:12]}"
