from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' - ' + self.email
