from django.db import models


# Create your models here.


class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    sender = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    creation_date = models.CharField(max_length=20)
    isRead = models.BooleanField(default=False)

    def __str__(self):
        return("{'id': %s, 'sender': %s, 'receiver': %s, 'creation_date': %s, 'subject': %s, 'content': %s, 'isRead': %s}" % (self.id, self.sender, self.receiver, self.creation_date, self.subject, self.content, self.isRead))
