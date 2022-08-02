from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class OnePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    body = models.TextField()
    abstract = models.TextField(default="abstract", max_length=256)
    imgurl = models.URLField(default="https://s2.loli.net/2022/08/01/8KSLDNbVMiFxgI4.jpg",max_length=256)
    createTime = models.DateTimeField(default=timezone.now)
    updateTime = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-createTime',)

    def __str__(self):
        return self.title
