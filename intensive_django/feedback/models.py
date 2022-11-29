from django.db import models


class FeedBack(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=1000)
